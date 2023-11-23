from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def link01(request):
    return render(request, 'PRUEBA/index.html')
