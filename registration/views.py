import json
from datetime import datetime

import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from .models import Participant, Child
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
        question_1 = data.get('question_1')
        question_2 = data.get('question_2')
        question_3 = data.get('question_3')
        question_4 = data.get('question_4')
        question_5 = data.get('question_5')
        question_6 = data.get('question_6')
        question_7 = data.get('question_7')
        arrival_date = data.get('arrival_date')

        # generation 7
        total_number = float(data.get('total_number')) if data.get('total_number') else 0
        spouse_name = data.get('spouse_name')
        child_name = data.getlist('child_name')
        child_age = data.getlist('child_age')

        if total_number == 0 and question_3 == "Yes":
            total_number = 1

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
            question_1=question_1,
            question_2=question_2,
            question_3=question_3,
            question_4=question_4,
            question_5=question_5,
            question_6=question_6,
            question_7=question_7,
            arrival_date=arrival_date,
            spouse_name=spouse_name,
            gen7_total_attendees=total_number,
            payment_reference=payment_reference
        )

        for i, j in zip(child_name, child_age):
            if i and j:
                Child.objects.create(
                    participant=participant,
                    name=i,
                    age=int(j)
                )

        payment_context = {
            "total_amount": float(2000 + (total_number * 100)),
            "gen7_amount": float(total_number * 100),
            "gen7_total_number": int(total_number),
            "gen7_attendee": True if question_3 == "Yes" else False,
            "reference": payment_reference,

        }

        return render(request, 'registration/payment.html', payment_context)
    return render(request, 'registration/index.html')


def payment(request):
    return render(request, 'registration/payment.html')


class CheckoutView(View):
    template_name = 'exclusive/payment.html'

    def get(self, request):
        quantity = request.GET.get('quantity', 1)
        amount = 200000 + (10000 * int(quantity))
        reference = request.GET.get('reference')

        # get participant email
        participant = Participant.objects.get(payment_reference=reference)
        email = participant.email

        hostname = request.get_host()

        url = "https://api.paystack.co/transaction/initialize"

        payload = json.dumps({
            "email": email,
            "amount": amount,
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
            p = Participant.objects.get(payment_reference=reference)
            p.paid = True
            p.save()

        print(context)
        return render(request, self.template_name, context)

