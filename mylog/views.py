# mylog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import User
from .models import Product


def home(request):
    products = Product.objects.all()  
    return render(request, 'index.html', {'productss': products})

def login_register_view(request):
    if request.user.is_authenticated:
        return redirect('')  
    return render(request, 'auth/login_register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('')  
            else:
                messages.error(request, 'Credenciales inválidas')
        except User.DoesNotExist:
            messages.error(request, 'No existe un usuario con este correo')
    return redirect('login_register')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        name = request.POST.get('name', '')
        last_name = request.POST.get('last_name', '')
        
        # Validaciones básicas
        if password1 != password2:
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('login_register')
            
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Este correo ya está registrado')
            return redirect('login_register')
            
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Este nombre de usuario ya está en uso')
            return redirect('login_register')
            
        try:
            user = User.objects.create(
                username=username,
                email=email,
                password=make_password(password1), 
                name=name,
                last_name=last_name,
                role=1,  
            )
            login(request, user)
            messages.success(request, 'Registro exitoso!')
            return redirect('') 
            
        except Exception as e:
            messages.error(request, f'Error en el registro: {str(e)}')
            
    return redirect('login_register')