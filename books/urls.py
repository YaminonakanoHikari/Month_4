from django.urls import path
from . import views

urlpatterns = [
    path('time/', views.current_time),
    path('random/', views.random_number),
    path('about/', views.about_me),
]