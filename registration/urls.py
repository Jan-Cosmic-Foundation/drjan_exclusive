from django.urls import path
from . import views

app_name = 'registration'
urlpatterns = [
    path('register/', views.index, name='register'),
    path('payment/', views.payment, name='payment'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('confirm-payment/', views.ConfirmPaymentView.as_view(), name='confirm-payment'),
]