from django.shortcuts import render
from .models import *


def index(request):
    courses_ = Course.objects.all()
    context = {
        "courses": courses_
    }
    return render(request, 'exclusive/index.html', context)


def course_index(request):
    courses_ = Course.objects.all()
    context = {
        "courses": courses_
    }
    return render(request, 'exclusive/main-landing.html', context)


def courses(request):
    courses_ = Course.objects.filter(core=True).order_by('course_number')

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

    next_lesson = lesson.lesson_number + 1
    if next_lesson <= course.lessons.count():
        next_lesson = course.lessons.get(lesson_number=next_lesson)
    else:
        next_lesson = None

    # check language
    twi = False
    if request.GET.get('language'):
        if request.GET.get('language') == 'twi':
            twi = True

    context = {
        'course': course,
        'lesson': lesson,
        'related_lessons': related_lessons,
        'next_lesson': next_lesson,
        'twi': twi
    }
    return render(request, 'exclusive/single-lesson.html', context)


def faqs(request):
    return render(request, 'exclusive/faq.html')


def contact(request):
    return render(request, 'exclusive/contact.html')


def pricing(request):
    return render(request, 'exclusive/pricing.html')
