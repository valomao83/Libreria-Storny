from django.http import request
from django.shortcuts import render, redirect

def Login():
    return render(request, "Storni/Login.html")

def Registro(request):
    return render(request, "Storni/Registro.html")

    