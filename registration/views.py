from django.http import HttpResponse
from django.shortcuts import render


def register(request):
    return render(request, 'registration/index.html')


def index(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        return HttpResponse('Data received')
    return render(request, 'registration/index.html')