# app_two/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='app_two_index'),
]
