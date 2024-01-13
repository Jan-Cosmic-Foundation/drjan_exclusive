from django.urls import path
from . import views

app_name = 'course'
urlpatterns = [
    path('', views.index, name='index'),
    path('pathways/', views.pathways, name='pathways'),
    path('lessons/', views.lessons, name='lessons'),
    path('lesson_detail/', views.lesson_detail, name='lesson_detail'),
    path('pathway_detail/', views.pathway_detail, name='pathway_detail'),
    path('faqs/', views.faqs, name='faqs'),
    path('contact/', views.contact, name='contact'),
    path('pricing/', views.pricing, name='pricing'),
]