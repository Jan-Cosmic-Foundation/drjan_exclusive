import json
from datetime import datetime

import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from .models import Participant, Child, Donation
import random
import string


def register(request):
    return render(request, 'registration/index.html')


def generate_payment_reference():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))


def index(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        email = data.get('email')
        phone = data.get('phone')
        country = data.get('country')
        dob = data.get('dob')
        gender = data.get('gender')
        region = data.get('region')
        transport = data.get('transport')
        personal_transport = data.get('personalTransport')
        impartation = data.get('impartation')
        registered_student = data.get('registeredStudent')
        attending_gtc = data.get('attendingGuideTheChildren')
        total_attending_gtc = data.get('TotalAttendingGuideTheChildren')
        accommodation = data.get('accommodation')
        arrival_date = data.get('arrivalDate')
        volunteering = data.get('volunteering')
        comments = data.get('comments')

        # generate payment reference
        payment_reference = generate_payment_reference()

        # Convert date of birth (dob) string to date object
        dob = datetime.strptime(dob, '%Y-%m-%d').date() if dob else None

        # Convert arrival date string to date object
        arrival_date = datetime.strptime(arrival_date, '%Y-%m-%d').date() if arrival_date else None

        participant = Participant.objects.create(
            first_name=firstname,
            last_name=lastname,
            email=email,
            phone=phone,
            country=country,
            dob=dob,
            gender=gender,
            impartation=impartation,
            registered_student=registered_student,
            attending_gtc=attending_gtc,
            total_attending_gtc=total_attending_gtc,
            accommodation=accommodation,
            arrival_date=arrival_date,
            volunteering=volunteering,
            comments=comments,
            region=region,
            transport=transport,
            personal_transport=personal_transport,
            payment_reference=payment_reference
        )

        # payment_context = {
        #     "total_amount": float(2000 + (total_number * 100)),
        #     "gen7_amount": float(total_number * 100),
        #     "gen7_total_number": int(total_number),
        #     "gen7_attendee": True if question_3 == "Yes" else False,
        #     "reference": payment_reference,
        #
        # }

        return render(request, 'registration/payment.html')
    return render(request, 'registration/index.html')


def payment(request):
    context = {}
    if request.GET:
        support = request.GET.get('supportTo')

        context['support'] = support
    return render(request, 'registration/payment.html', context)


def analytics(request):
    participants = Participant.objects.all()
    total = participants.count()

    children = Child.objects.all()
    total_children = children.count()

    q_3 = participants.filter(question_3='Yes')
    total_gen7 = q_3.count()

    for p in participants:
        if p.spouse_name:
            total_gen7 += 1

        total_gen7 += p.children.count()

    # number of participants not in ghana
    p_not_ghana = 0
    for p in participants:
        if p.country != 'Ghana':
            p_not_ghana += 1

    total_spouse = 0
    for p in participants:
        if p.spouse_name:
            total_spouse += 1

    context = {
        'total': total,
        'total_students_coming_GTC': q_3.count(),
        'total_spouse': total_spouse,
        'total_children': total_children,
        'total_gen7': total_gen7,
        'total_not_ghana': p_not_ghana,
    }
    return render(request, 'registration/analytics.html', context)


class CheckoutView(View):
    template_name = 'exclusive/payment.html'

    def get(self, request):
        amount = request.GET.get('amount')
        reference = request.GET.get('reference')
        email = request.GET.get('email')
        name = request.GET.get('name')
        project = request.GET.get('project')

        reference = generate_payment_reference() if not reference else reference

        # create donation record
        Donation.objects.create(
            name=name,
            email=email,
            reference=reference,
            project=project,
            amount=float(amount),
        )

        # # get participant email
        # participant = Participant.objects.get(payment_reference=reference)
        # email = participant.email

        hostname = request.get_host()

        url = "https://api.paystack.co/transaction/initialize"

        payload = json.dumps({
            "email": email,
            "amount": float(amount) * 100,
            "callback_url": f"http://{hostname}/event-registration/confirm-payment/",
            "reference": reference,
            "channels": [
                "mobile_money",
                "card",
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


class ConfirmPaymentView(View):
    template_name = 'registration/payment_successful.html'

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
            d = Donation.objects.get(reference=reference)
            d.paid = True
            d.save()

        print(context)
        return render(request, self.template_name, context)

