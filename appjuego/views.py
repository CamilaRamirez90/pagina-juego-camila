from django.shortcuts import render
from django.http import HttpResponse

def hola_mundo(request):
    return HttpResponse('Alo')

# Create your views here.
