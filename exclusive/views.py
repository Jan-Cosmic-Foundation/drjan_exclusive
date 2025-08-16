import json
from django.http import HttpResponseRedirect
from django.urls import reverse
import requests
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail

from .models import *
from .decorators import require_registered_user


# class IndexView(View):
#     template_name = 'exclusive/index.html'
#
#     def get(self, request):
#         courses_ = Course.objects.all()
#         context = {
#             "courses": courses_
#         }
#         return render(request, self.template_name, context)


class CourseIndexView(View):
    template_name = 'exclusive/main-landing.html'

    # login_url = '/login/'

    def get(self, request):
        courses_ = Course.objects.all()
        context = {
            "courses": courses_
        }
        return render(request, self.template_name, context)


class CoursesView(LoginRequiredMixin, View):
    template_name = 'exclusive/pathways.html'
    login_url = '/login/'

    @require_registered_user
    def get(self, request):
        courses_ = Course.objects.filter(core=True).order_by('course_number')
        context = {
            'courses': courses_,
        }
        return render(request, self.template_name, context)


class CourseDetailView(LoginRequiredMixin, View):
    template_name = 'exclusive/single-course.html'
    login_url = '/login/'

    @require_registered_user
    def get(self, request, course_id):
        return render(request, self.template_name)


class LessonsView(LoginRequiredMixin, View):
    template_name = 'exclusive/lessons.html'
    login_url = '/login/'

    @require_registered_user
    def get(self, request, course_slug):
        course_ = Course.objects.get(slug=course_slug)
        course_lessons = course_.lessons.all()

        context = {
            'course': course_,
            'course_lessons': course_lessons,
        }
        return render(request, self.template_name, context)


class LessonDetailView(LoginRequiredMixin, View):
    template_name = 'exclusive/single-lesson.html'
    login_url = '/login/'

    @require_registered_user
    def get(self, request, course_slug, lesson_slug):
        course = Course.objects.get(slug=course_slug)
        lesson = Lesson.objects.get(slug=lesson_slug)
        course_lessons = course.lessons.all()

        next_lesson = lesson.lesson_number + 1
        if next_lesson <= course.lessons.count():
            next_lesson = course.lessons.get(lesson_number=next_lesson)
        else:
            next_lesson = None

        twi = False
        if request.GET.get('language') and request.GET.get('language') == 'twi':
            twi = True

        context = {
            'course': course,
            'lesson': lesson,
            'course_lessons': course_lessons,
            'next_lesson': next_lesson,
            'twi': twi
        }
        return render(request, self.template_name, context)


class FAQsView(View):
    template_name = 'exclusive/faq.html'

    def get(self, request):
        return render(request, self.template_name)


class ContactView(View):
    template_name = 'exclusive/contact.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        Comment.objects.create(name, email, message)

        # Reverse the URL to redirect after the comment is created
        return HttpResponseRedirect(reverse('comment_success'))


class PricingView(View):
    template_name = 'exclusive/pricing.html'

    def get(self, request):
        # if the user is already registered, redirect to the course index
        if request.user.is_authenticated and request.user.profile.registered:
            return redirect('course:index')
        return render(request, self.template_name)


# =============================================== Payment ===============================================

class CheckoutView(LoginRequiredMixin, View):
    template_name = 'exclusive/payment.html'
    login_url = '/login/'

    def get(self, request):
        amount = 100
        email = request.user.email

        url = "https://api.paystack.co/transaction/initialize"

        payload = json.dumps({
            "email": email,
            "amount": amount,
            "callback_url": "https://awake.drbaffourjan.com/confirm-payment/",
            "split_code": "SPL_NB7LnX54qz",
            "channels": [
                "card",
                "mobile_money"
            ]
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {settings.PAYSTACK_SECRET_KEY}'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        response_data = response.json()
        print(response_data)
        return redirect(response_data['data']['authorization_url'])


class ConfirmPaymentView(LoginRequiredMixin, View):
    template_name = 'exclusive/confirm-payment.html'
    login_url = '/login/'

    def get(self, request):
        context = {}
        reference = request.GET.get('reference')
        trxref = request.GET.get('trxref')

        url = f"https://api.paystack.co/transaction/verify/{reference}"

        headers = {
            'Authorization': f'Bearer {settings.PAYSTACK_SECRET_KEY}',
        }

        response = requests.request("GET", url, headers=headers)
        response_data = response.json()

        status = response_data['data']['status']
        amount = response_data['data']['amount']

        context['status'] = status

        if status == 'success':
            # update the user registration status
            user = request.user
            user.profile.registered = True
            user.profile.save()

            # save in payments
            p = Payment(user, amount)
            p.save()

        return render(request, self.template_name, context)


# =============================================== Auth ===============================================
class LoginView(View):
    template_name = 'exclusive/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, self.template_name, {'error': 'Invalid email or password'})

        if user.check_password(password):
            auth_user = authenticate(request, username=user.username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('course:index')  # todo: if the user is not registered redirect to pricing
        return render(request, self.template_name, {'error': 'Invalid email or password'})


class SignupView(View):
    template_name = 'exclusive/signup.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            return render(request, self.template_name, {'error': 'Email is already registered. Try Logging in.'})

        user = User.objects.create_user(username=email.split("@")[0], email=email, password=password)

        try:
            user.first_name, user.last_name = full_name.split(maxsplit=1)
        except ValueError:
            user.first_name = full_name

        user.save()

        profile = Profile(user=user)
        profile.save()

        login(request, user)

        return redirect('course:index')
        # return redirect('course:checkout')


class ProfileView(LoginRequiredMixin, View):
    template_name = 'exclusive/account-profile.html'
    login_url = "/login/"

    def get(self, request):
        # get current user
        user = request.user
        context = {
            "user": user
        }
        return render(request, self.template_name, context)


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('course:login')


# =========================================== password reset ==============================================
def password_reset_request(request):
    error = None
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(email=data)
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "exclusive/password/password_reset_email.html"
                    c = {
                        "email": user.email,
                        'domain': get_current_site(request).domain,
                        'site_name': 'Your Site Name',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    send_mail(subject, email, settings.DEFAULT_FROM_EMAIL, [user.email], fail_silently=False,
                              html_message=email)
                return redirect("/password_reset/done/")
            else:
                error = "Email is not registered."
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="exclusive/password/password_reset.html",
                  context={"password_reset_form": password_reset_form, "error": error})


def password_reset_done(request):
    return render(request=request, template_name="exclusive/password/password_reset_done.html")


def password_reset_confirm(request, uidb64=None, token=None):
    error = None
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=uid)

    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('/reset/done/')
        else:
            error = form.errors.get('new_password2', None)[0]
            print(error)
    else:
        form = SetPasswordForm(user)

    context = {
        'form': form,
        'uidb64': uidb64,
        'token': token,
        'error': error,
    }

    return render(request, 'exclusive/password/password_reset_confirm.html', context)


def password_reset_complete(request):
    return render(request=request, template_name="exclusive/password/password_reset_complete.html")
