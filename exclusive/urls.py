from django.urls import path
from . import views

app_name = 'course'
urlpatterns = [
    path('', views.course_index, name='index'),
    path('index/', views.index, name='c_index'),
    path('courses/', views.courses, name='courses'),
    path('courses/<slug:course_slug>', views.course_detail, name='course_detail'),
    path('lessons/<slug:course_slug>', views.lessons, name='lessons'),
    path('lessons/<slug:course_slug>/<slug:lesson_slug>', views.lesson_detail, name='lesson'),
    path('faqs/', views.faqs, name='faqs'),
    path('contact/', views.contact, name='contact'),
    path('pricing/', views.pricing, name='pricing'),
]