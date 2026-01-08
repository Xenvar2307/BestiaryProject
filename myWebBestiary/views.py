#from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    #return HttpResponse("Home page welcome message!")
    return render(request, "home.html")

def aboutPage(request):
    #return HttpResponse("This is info about app you are using!")
    return render(request, "about.html")