from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Course, Lesson, Profile


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
                return redirect('course:index')
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
            return render(request, self.template_name, {'error': 'Email already in use.'})

        user = User.objects.create_user(username=email.split("@")[0], email=email, password=password)
        user.first_name, user.last_name = full_name.split(maxsplit=1)
        user.save()

        profile = Profile(user=user)
        profile.save()

        login(request, user)

        return redirect('course:index')


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


# class IndexView(View):
#     template_name = 'exclusive/index.html'
#
#     def get(self, request):
#         courses_ = Course.objects.all()
#         context = {
#             "courses": courses_
#         }
#         return render(request, self.template_name, context)


class CourseIndexView(LoginRequiredMixin, View):
    template_name = 'exclusive/main-landing.html'
    login_url = '/login/'

    def get(self, request):
        courses_ = Course.objects.all()
        context = {
            "courses": courses_
        }
        return render(request, self.template_name, context)


class CoursesView(LoginRequiredMixin, View):
    template_name = 'exclusive/pathways.html'
    login_url = '/login/'

    def get(self, request):
        courses_ = Course.objects.filter(core=True).order_by('course_number')
        context = {
            'courses': courses_,
        }
        return render(request, self.template_name, context)


class CourseDetailView(LoginRequiredMixin, View):
    template_name = 'exclusive/single-course.html'
    login_url = '/login/'

    def get(self, request, course_id):
        return render(request, self.template_name)


class LessonsView(LoginRequiredMixin, View):
    template_name = 'exclusive/lessons.html'
    login_url = '/login/'

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


class ContactView(LoginRequiredMixin, View):
    template_name = 'exclusive/contact.html'

    def get(self, request):
        return render(request, self.template_name)


class PricingView(LoginRequiredMixin, View):
    template_name = 'exclusive/pricing.html'
    login_url = '/login/'

    def get(self, request):
        return render(request, self.template_name)


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('course:login')

