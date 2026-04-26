from django.urls import path
from . import views

app_name = 'vaesen'

urlpatterns = [
    path("", views.homePage, name="home"),
   
]
