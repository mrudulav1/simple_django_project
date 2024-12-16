# app_two/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'app_two/index.html', {'message': 'Hello from App Two!'})
