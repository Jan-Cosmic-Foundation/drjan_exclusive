from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'exclusive/index.html')


def lesson(request):
    return render(request, 'exclusive/single-lesson.html')


def lessons(request):
    return render(request, 'exclusive/lessons.html')

def pathways(request):
    return render(request, 'exclusive/pathways.html')