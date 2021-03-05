from django.contrib import admin
from django.urls import path,include
from app1 import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('contact',views.contact,name='contact'),
    path('forts',views.forts,name='forts'),
    path('beaches',views.beaches,name='beaches'),
    path('museum',views.museum,name='museum'),
    path('caves',views.caves,name='caves'),
    path('hot_water_springs',views.hot_water_springs,name='hot_water_springs'),
    path('temples',views.temples,name='temples')
]
