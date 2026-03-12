from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'static_handler.html', {})

def home2(request):
    return HttpResponse('Привет, Мир!')
