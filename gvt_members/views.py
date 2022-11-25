from django.shortcuts import render
from .models import *


def home(request):
    return render(request, 'main.html', {'national':national})

def governors(request):
    governors = Governors.objects.all()
    context = {'governors':governors}

    return render(request, 'governors.html', context)

def national(request):
    national = National.objects.all()
    presidential = national.filter(category='Presidential')
    cabinet = national.filter(category='Cabinet')

    context = {'presidential':presidential, 'cabinet':cabinet}
    return render(request, 'national.html', context)

def senators(request):
    senators = Senators.objects.all()
    context = {'senators':senators}

    return render(request, 'senators.html', context)

def womenrepresentatives(request):
    womenrepresentatives = Womenrepresentatives.objects.all()
    context = {'womenrepresentatives':womenrepresentatives}

    return render(request, 'womenrepresentatives.html', context)

