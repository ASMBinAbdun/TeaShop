from django.shortcuts import render
from django.http import HttpResponse
from . models import Tea


def home(request):
    tea = Tea.objects.all()
    return render(request, "home.html", {"tea":tea})

def tea(request):
    tea = Tea.objects.all()
    return render(request, "tea.html", {"tea" : tea})

