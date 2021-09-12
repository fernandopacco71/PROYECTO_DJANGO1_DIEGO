from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    return HttpResponse("<center><h1>Pagina principal</h1></center>")

def vender(request):
    return HttpResponse("<center><h1>Pagina para realizar ventas</h1></center>")

def nuevo(request):
    return HttpResponse("<center><h1>Pagina para agregar nuevo producto</h1></center>")
