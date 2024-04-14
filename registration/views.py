import json
import requests
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings


def register(request):
    return render(request, 'registration/index.html')


def index(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        return render(request, 'registration/payment.html')
    return render(request, 'registration/index.html')


def payment(request):
    return render(request, 'registration/payment.html')


class CheckoutView(View):
    template_name = 'exclusive/payment.html'

    def get(self, request):
        event = request.GET.get('event')
        quantity = request.GET.get('quantity', 1)
        amount = 200000 if event == 'main' else 10000 * int(quantity)
        email = "somehing@gmail.com"

        url = "https://api.paystack.co/transaction/initialize"

        payload = json.dumps({
            "email": email,
            "amount": amount,
            "callback_url": "https://awake.drbaffourjan.com/confirm-payment/",
            "channels": [
                "mobile_money"
                "card",
            ]
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {settings.PAYSTACK_SECRET_KEY}'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        response_data = response.json()

        return redirect(response_data['data']['authorization_url'])


class ConfirmPaymentView(View):
    template_name = 'exclusive/confirm-payment.html'

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
            user = request.user
            user.profile.registered = True
            user.profile.save()

        print(context)
        return render(request, self.template_name, context)

