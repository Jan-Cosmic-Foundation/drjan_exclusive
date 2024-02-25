from django.urls import path
from .views import *

app_name = 'course'
urlpatterns = [
    path('', CourseIndexView.as_view(), name='index'),
    path('index/', IndexView.as_view(), name='c_index'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('courses/', CoursesView.as_view(), name='courses'),
    path('courses/<slug:course_slug>', CourseDetailView.as_view(), name='course_detail'),
    path('lessons/<slug:course_slug>', LessonsView.as_view(), name='lessons'),
    path('lessons/<slug:course_slug>/<slug:lesson_slug>', LessonDetailView.as_view(), name='lesson'),
    path('faqs/', FAQsView.as_view(), name='faqs'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('pricing/', PricingView.as_view(), name='pricing'),
]