from django.shortcuts import render

from website.templates import*

def landing_page(request):
    return render(request,'diginstruments.html')

def login_page(request):
    return render(request,'login.html')

def guitarras_page(request):
    return render(request,'guitarras.html')
def baterias_page(request):
    return render(request,'baterias.html')
def violines_page(request):
    return render(request,'violines.html')
def teclados_page(request):
    return render(request,'teclados.html')
def flautas_page(request):
    return render(request,'flautas.html')
def sax_page(request):
    return render(request,'sax.html')