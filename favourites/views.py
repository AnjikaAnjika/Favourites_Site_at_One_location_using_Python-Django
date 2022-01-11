#This is the page created by - Anjika

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def feedback(request):
    return render(request, 'feedback.html')



