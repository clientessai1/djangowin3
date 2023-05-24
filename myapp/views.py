from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse;

def home(request):
    return render(request, 'home.html'); #HttpResponse("<h2>Bienvenue !</h2>");
