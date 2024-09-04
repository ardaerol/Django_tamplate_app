from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request,"template_app/first.html")



def weather_view(request):
    weather_dictionary = {
        "Istanbul" : "30",
        "Amsterdam" : "20",
        "Elazığ" : "25",
        "Paris" : [5,14,22,21],
        "rome" : {"morning" : 22, "night": 10},
        "user_premium" : True,
        "test" : "Test test TesT TEST"
    }
    return render(request,"template_app/weather.html",context=weather_dictionary)