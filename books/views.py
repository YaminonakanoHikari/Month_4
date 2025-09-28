from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime
import random

def current_time(request):
    return HttpResponse(f"Текущее время: {datetime.now()}")

def random_number(request):
    return HttpResponse(f"Случайное число: {random.randint(1, 100)}")

def about_me(request):
    return HttpResponse("Привет, я Ариана! Я начинаю изучать Django :)")

