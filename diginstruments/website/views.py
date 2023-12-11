from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/landing_page')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.', extra_tags='alert-danger')

    return render(request, 'login.html')

def register_page(request):
    return render(request, 'register.html')

# def login_page(request):
#     if (request.method) == 'POST':
#         username = request.POST ['username']
#         password = request.POST ['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect ('/landing_page')
#     elif request.method == 'GET':
#         return render(request, 'login.html')

def landing_page(request):
    return render(request,'diginstruments.html')
def logout_page(request):
    logout(request)
    return redirect('/')
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