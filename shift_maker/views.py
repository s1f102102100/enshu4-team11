from django.shortcuts import render

# Create your views here.
# Create your views here.
def index(request):
    return render(request, "shift_maker/login.html")

def choice_page(request):
    return render(request, "shift_maker/choice_page.html")

def default(request):
    return render(request, "shift_maker/default.html")

def irregular(request):
    return render(request, "shift_maker/irregular.html")


