from django.urls import path
from . import views

app_name = 'statblocks'

urlpatterns = [
    path("", views.statblocks_list, name='list'),
    path("/traits_list", views.traits_list, name='traits_list'),
    path('<slug:slug>', views.statblock_page, name='page'),
    
]
