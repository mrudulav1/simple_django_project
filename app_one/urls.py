# app_one/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='app_one_index'),
]
