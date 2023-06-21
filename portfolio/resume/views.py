#from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello everyone. If you are interested, here is my RESUME...")

