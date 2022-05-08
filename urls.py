from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [

    path('',views.home,name='home'),
    path('register/add/', views.add, name='add'),
    path('register/', views.register, name='register'),




]