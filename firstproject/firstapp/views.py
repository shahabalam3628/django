from django.shortcuts import render
from firstapp import views
from django.http import HttpResponse    # for HttpResponse()

def welcome(request):
    return HttpResponse("Welcome in DJango")

def about(request):
    return render(request,'about.html')

def services(request):
     return render(request,'services.html')

def projects(request):
     return render(request,'projects.html')

def courses(request):
    return render(request,'courses.html')

def codes(request):   
    return render(request,'codes.html')

def contact(request):
    return render(request,'contact.html')     

def home(request):
    return render(request,'index.html')

def templates_demo(request):
    return render(request,'welcome.html')   
def call_app_url(request):
    return render(request,'welcome.html') 
def insert_demo(request):
    return render(request,'insert.html')    

