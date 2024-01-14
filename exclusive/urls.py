from django.urls import path
from . import views

app_name = 'course'
urlpatterns = [
    path('', views.index, name='index'),
    path('courses/', views.courses, name='courses'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('lessons/<int:course_id>', views.lessons, name='lessons'),
    path('lessons/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('faqs/', views.faqs, name='faqs'),
    path('contact/', views.contact, name='contact'),
    path('pricing/', views.pricing, name='pricing'),
]