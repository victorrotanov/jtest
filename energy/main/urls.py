from html import entities
from django.shortcuts import render
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='main'),
    path('contact/', contacts, name='contact'),
    path('history/', history, name='history'),
    path('managment/', managment, name='managment'),
    path('procurement/', procurement, name='procurement'),
    path('strategy/', strategy, name='strategy'),
    path('outages/', outages, name='outages'),
    path('evolution/', evolution, name='evolution'),
    path('investments/', investments, name='investments'),
    path('meter_readings/', meter_readings, name='meter_readings'),
    path('individuals/', individuals, name='individuals'),
    path('entities/', entities, name='entities'),
    path('techspec/', techspec, name='techspec'),
    path('plunder/', plunder, name='plunder'),
    path('esaving/', esaving, name='esaving'),
    path('stap/', stap, name='stap'),
    path('points/', points, name='points'),
    path('payments/', payments, name='payments'),
    path('tariffs/', tariffs, name='tariffs'),
    path('warmth/', warmth, name='warmth'),
    path('question/', question, name='question'),
    path('training/', training, name='training'),
    path('ourprofs/', ourprofs, name='ourprofs'),
    path('success/', success, name='success'),
]
