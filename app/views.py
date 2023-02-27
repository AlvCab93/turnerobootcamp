from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Este es el Sistema Turnero")

def Inicio(request):
    return render(request,"inicio.html",{})