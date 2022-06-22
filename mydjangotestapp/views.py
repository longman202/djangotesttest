from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def home(request):
    '''Renders the home page'''
    return render(request, 'index.html') 