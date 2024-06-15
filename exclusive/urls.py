from django.urls import path
from .views import *
from django.urls import path


app_name = 'course'
urlpatterns = [
    path('', CourseIndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('courses/', CoursesView.as_view(), name='courses'),
    path('courses/<slug:course_slug>', CourseDetailView.as_view(), name='course_detail'),
    path('lessons/<slug:course_slug>', LessonsView.as_view(), name='lessons'),
    path('lessons/<slug:course_slug>/<slug:lesson_slug>', LessonDetailView.as_view(), name='lesson'),
    path('faqs/', FAQsView.as_view(), name='faqs'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('pricing/', PricingView.as_view(), name='pricing'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('confirm-payment/', ConfirmPaymentView.as_view(), name='confirm_payment'),
    path('logout/', LogoutView.as_view(), name='logout'),
     path('password_reset/', password_reset_request, name='password_reset'),
    path('password_reset/done/', password_reset_done, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', password_reset_complete, name='password_reset_complete'),
]