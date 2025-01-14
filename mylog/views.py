from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from decimal import Decimal, InvalidOperation
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from .models import User, Product

def home(request):
    # Obtén todos los productos y pásalos al template
    products = Product.objects.all()  
    return render(request, 'index.html', {'products': products})


def login_register_view(request):
    print(f"Usuario autenticado: {request.user.is_authenticated}")
    if request.user.is_authenticated:
        return redirect('mylog:home') 
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
                return redirect('mylog:home') 
            else:
                messages.error(request, 'Credenciales inválidas')
        except User.DoesNotExist:
            messages.error(request, 'No existe un usuario con este correo')
    return redirect('mylog:login_register')


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
            return redirect('mylog:login_register')   
            
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Este correo ya está registrado')
            return redirect('mylog:login_register')  
            
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Este nombre de usuario ya está en uso')
            return redirect('mylog:login_register')   
            
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
            return redirect('mylog:login_register')  
            
        except Exception as e:
            messages.error(request, f'Error en el registro: {str(e)}')
            
    return redirect('mylog:login_register')

def custom_logout(request):
    logout(request)
    return redirect('mylog:home') 




@login_required(login_url='mylog:login_register') 
def addProduct(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')

        try:
            price = Decimal(request.POST.get('price'))
        except InvalidOperation:
            messages.error(request, 'El precio debe ser un número válido.')
            return redirect('mylog:addproduct')

        stock = request.POST.get('stock')
        features = request.POST.get('features', '')
        imgs = request.FILES.get('imgs')  

        try:
            product = Product.objects.create( 
                name=name,
                description=description,
                price=price, 
                stock=stock,
                features=features,
                imgs=imgs, 
            )
            messages.success(request, 'Producto registrado con éxito')
            return redirect('mylog:home')
        except Exception as e:
            messages.error(request, f'Error al registrar el producto: {str(e)}')
            return redirect('mylog:addproduct') 
    return render(request, 'pages/FormProduct.html')


@login_required(login_url='mylog:login_register') 
def userP(request, name):
    user = get_object_or_404(User, username=name) 
    users = User.objects.all() 
    return render(request, 'pages/UserP.html', {'user': user, 'users': users})
