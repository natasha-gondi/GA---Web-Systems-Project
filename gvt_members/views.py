from django.shortcuts import render
from .models import *


def home(request):
    return render(request, 'main.html', {'national':national})

def governors(request):
    return render(request, 'governors.html')

def national(request):
    national = National.objects.all()
    presidential = national.filter(category='Presidential')

    context = {'presidential':presidential}
    return render(request, 'national.html', context)
