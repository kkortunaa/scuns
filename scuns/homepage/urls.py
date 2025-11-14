from django.contrib import admin
from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('list/', views.scuns_list, name='list'),
    path("<int:pk>/delete/", views.delete_user, name="delete"), 
] 
