from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from decimal import Decimal, InvalidOperation
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from .models import User, Product, Cart
from django.http import JsonResponse
import json

def home(request):
    products = Product.objects.all()  
    return render(request, 'index.html', {'products': products})

def login_register_view(request):
    if request.user.is_authenticated:
        return redirect('mylog:home') 
    return render(request, 'auth/login_register.html')  

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Debug: Imprimir información de la solicitud
        print("==== Debug Info ====")
        print(f"Método: {request.method}")
        print(f"Email recibido: {email}")
        print(f"¿Contraseña recibida?: {'Sí' if password else 'No'}")
        print(f"POST data: {request.POST}")
        
        if not email or not password:
            print("Error: Email o contraseña faltante")
            messages.error(request, 'Por favor ingrese email y contraseña')
            return redirect('mylog:login_register')
        
        try:
            # Primero verificar si el usuario existe
            try:
                user = User.objects.get(email=email)
                print(f"Usuario encontrado: {user.username}")
            except User.DoesNotExist:
                print("Usuario no encontrado")
                messages.error(request, 'Email o contraseña incorrectos')
                return redirect('mylog:login_register')
            
            # Intentar autenticación
            authenticated_user = authenticate(
                request,
                username=email,  # EMAIL como username
                password=password
            )
            
            print(f"Resultado de authenticate: {authenticated_user}")
            
            if authenticated_user is not None:
                login(request, authenticated_user)
                print(f"Login exitoso para: {authenticated_user.username}")
                messages.success(request, f'Bienvenido {authenticated_user.username}!')
                return redirect('mylog:home')
            else:
                print("Autenticación fallida")
                messages.error(request, 'Email o contraseña incorrectos')
                
        except Exception as e:
            print(f"Error inesperado: {str(e)}")
            messages.error(request, 'Error en el inicio de sesión')
            
    return redirect('mylog:login_register')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        name = request.POST.get('name', '')
        last_name = request.POST.get('last_name', '')
        
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
            messages.success(request, '¡Registro exitoso!')
            return redirect('mylog:home')
            
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
                user=request.user, 
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

@login_required(login_url='mylog:login_register')
def profile_view(request):
    return redirect('mylog:user_info')

@login_required(login_url='mylog:login_register')
def user_info(request):
    context = {
        'user': request.user
    }
    return render(request, 'pages/UserP.html', context)

@login_required(login_url='mylog:login_register')
def user_products(request):
    products = Product.objects.filter(user=request.user)
    context = {
        'products': products,
        'user': request.user
    }
    return render(request, 'pages/ProductP.html', context)

@login_required(login_url='mylog:login_register')
def update_user(request):
    if request.method == 'POST':
        user = request.user
        user.name = request.POST.get('name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.address = request.POST.get('address')
        
        password = request.POST.get('password')
        if password:
            user.password = make_password(password)
        
        if 'imgs' in request.FILES:
            user.imgs = request.FILES['imgs']
        
        user.save()
        messages.success(request, 'Información actualizada con éxito')
        return redirect('mylog:user_info')
    return redirect('mylog:user_info')

@login_required(login_url='mylog:login_register')
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, user=request.user)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.price = Decimal(request.POST.get('price'))
        product.stock = request.POST.get('stock')
        product.features = request.POST.get('features')
        if 'imgs' in request.FILES:
            product.imgs = request.FILES['imgs']
        product.save()
        messages.success(request, 'Producto actualizado con éxito')
        return redirect('mylog:user_products')
    return render(request, 'pages/ProductPM.html', {'product': product})

@login_required(login_url='mylog:login_register')
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, user=request.user)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Producto eliminado con éxito')
        return redirect('mylog:user_products')
    return redirect('mylog:user_products')

@login_required(login_url='mylog:login_register')
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user, active=True)
    total_price = sum(item.total_price() for item in cart_items)
    return render(request, 'pages/Cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required(login_url='mylog:login_register')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product, active=True)
    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity
    cart_item.save()
    messages.success(request, 'Producto añadido al carrito')
    return redirect('mylog:cart')

@login_required(login_url='mylog:login_register')
def update_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item_id = data.get('item_id')
        quantity = int(data.get('quantity'))
        
        cart_item = get_object_or_404(Cart, id=item_id, user=request.user, active=True)
        if quantity > 0 and quantity <= cart_item.product.stock:
            cart_item.quantity = quantity
            cart_item.save()
            
            cart_items = Cart.objects.filter(user=request.user, active=True)
            total_price = sum(item.total_price() for item in cart_items)
            
            return JsonResponse({
                'success': True,
                'item_total': cart_item.total_price(),
                'cart_total': total_price
            })
    return JsonResponse({'success': False})

@login_required(login_url='mylog:login_register')
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id, user=request.user, active=True)
    cart_item.delete()
    messages.success(request, 'Producto eliminado del carrito')
    return redirect('mylog:cart')
