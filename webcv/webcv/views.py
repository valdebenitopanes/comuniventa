from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import login as lg
from django.contrib.auth import logout as lgt
from django.contrib.auth import authenticate
#encriptar contraseña en texto plano
from django.contrib.auth.models import User, Group
from django.contrib import messages

# from django import forms
# Importar Clases de formulario
from .forms import Registro
from products.models import Product

def index(request):
    # return HttpResponse("saludo")
    products = Product.objects.all()

    return render(request, 'index.html', {
        'title': 'Tienda',
        'subtitle': 'Lista de productos',
        'products': products
        # 'products': [
        #     {'name': 'cocacola', 'stock': True, 'price': 1000},
        #     {'name': 'cerveza', 'stock': True, 'adult': 1200},
        #     {'name': 'pañales', 'stock': False, 'adult':3700 },
        #     {'name': 'alimento de gato', 'stock': True, 'adult': 1280}
        # ]
    })

def login(request):
    has_logged_out = 'SESSION_KEY' not in request.session
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        users = authenticate(username=username,password=password)
        if(users):
            lg(request,users) #validar documentation
            #print('LOGIN TRUE') #redireccionar
            messages.success(request,f'Bienvenido {users.username}')
            return redirect('index')
        else:
            #print('LOGIN FALSE') #variable de error
            messages.error(request,f'Datos incorrectos')
            # messages.error(request,f'Datos incorrectos 2')
    return render(request, 'users/login.html', {
        'has_logged_out':has_logged_out
    })

def logout(request):
    lgt(request)
    messages.success(request,'Sesión Cerrada')
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
  
    form = Registro(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        # username = form.cleaned_data.get('username')
        # email = form.cleaned_data.get('email')
        # password = form.cleaned_data.get('password')

        # usuario = User.objects.create_user(username,email,password)
        user = form.save()

        if user:
            lg(request,user)
            messages.success(request,f'Bienvenido ')
            return redirect('index')
        # print("request : ",request)
        # print("request POST ",request.POST)
        # print("user,email,pass : ",username,email,password)
        # {
        # 'username':'Patricia',
        # 'email':'pruebaregistro1@gmail.com'
        # }
        
    return render(request,'users/register.html',{
        'form':form
    })