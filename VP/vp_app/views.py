from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    # return render(request, 'bms_app/home.html')
    return HttpResponse("Hello, world. You're at the polls index.")


def homePage(request):
    # return render(request, 'bms_app/home.html')
    return HttpResponse("Home Page")
