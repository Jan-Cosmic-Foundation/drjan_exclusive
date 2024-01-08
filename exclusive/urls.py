from django.urls import path
from . import views

app_name = 'course'
urlpatterns = [
    path('', views.index, name='index'),
    path('lesson/', views.lesson, name='lesson'),
    path('pathways/', views.pathways, name='pathways'),
    path('lessons/', views.lessons, name='lessons'),
]