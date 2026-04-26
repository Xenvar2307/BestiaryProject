# Create your views here.
from django.shortcuts import render

def homePage(request):
    #return HttpResponse("Home page welcome message!")
    return render(request, "vaesen\home.html")