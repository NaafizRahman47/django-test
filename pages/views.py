from django.shortcuts import render
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('Hiiii!!!')

# Create your views here.
