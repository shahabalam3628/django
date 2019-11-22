from django.shortcuts import render
from firstapp import views
from django.http import HttpResponse    # for HttpResponse()

def welcome(request):
    return HttpResponse("Welcome in DJango")

def templates_demo(request):
    return render(request,'welcome.html')   
def call_app_url(request):
    return render(request,'welcome.html') 
