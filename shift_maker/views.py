from django.shortcuts import render
import pandas as pd



# Create your views here.
# Create your views here.

def choice_page(request):
    return render(request, "shift_maker/choice_page.html")

def default(request):
    return render(request, "shift_maker/default.html")

def irregular(request):
    return render(request, "shift_maker/irregular.html")

def start(request):
    return render(request, "shift_maker/start.html")

def making(request):
    return render(request, "shift_maker/making.html")

def brain(request):
    return render(request, "brain.py")



