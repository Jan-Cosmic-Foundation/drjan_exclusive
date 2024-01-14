from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request, 'exclusive/index.html')


def courses(request):
    courses_ = Course.objects.all()

    context = {
        'courses': courses_,
    }
    return render(request, 'exclusive/pathways.html', context)


def course_detail(request, course_id):
    return render(request, 'exclusive/single-course.html')


def lessons(request, course_slug):
    course_ = Course.objects.get(slug=course_slug)
    course_lessons = course_.lessons.all()

    context = {
        'course': course_,
        'course_lessons': course_lessons,
    }
    return render(request, 'exclusive/lessons.html', context)


def lesson_detail(request, course_slug, lesson_slug):
    course = Course.objects.get(slug=course_slug)
    lesson = Lesson.objects.get(slug=lesson_slug)
    related_lessons = course.lessons.all().exclude(slug=lesson_slug)

    context = {
        'course': course,
        'lesson': lesson,
        'related_lessons': related_lessons,
    }
    return render(request, 'exclusive/single-lesson.html', context)


def faqs(request):
    return render(request, 'exclusive/faq.html')


def contact(request):
    return render(request, 'exclusive/contact.html')


def pricing(request):
    return render(request, 'exclusive/pricing.html')
