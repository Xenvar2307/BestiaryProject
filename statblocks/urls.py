from django.urls import path
from . import views

app_name = 'statblocks'

urlpatterns = [
    path("", views.statblocks_list, name='list'),
    path("new_statblock/", views.statblock_new, name='new-statblock'),
    path('<slug:slug>', views.statblock_page, name='page'),

    path("/traits_list", views.traits_list, name='traits_list'),
]
