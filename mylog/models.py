from django.db import models
from django.contrib.auth.models import AbstractUser
from decimal import Decimal
from django.db import models
import os

# Extender el modelo User para incluir el rol y la dirección
class User(AbstractUser):
    name = models.CharField(max_length=100, default="Sin nombre")
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)  
    password = models.CharField(max_length=500)  
    imgs = models.ImageField(upload_to='uploads/UserProfile/', blank=True, default='uploads/default_profile_picture.jpg')
    ROLE_CHOICES = [
        (1, 'customer'),
        (2, 'admin'),
    ]
    role = models.IntegerField(choices=ROLE_CHOICES, default=1)
    address = models.CharField(max_length=255, blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='mylog_user_set',  
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='mylog_user_permissions',  
        blank=True
    )

    def __str__(self):
        return self.username


# Modelo de Producto
class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    features = models.TextField()  
    imgs = models.ImageField(upload_to='uploads/', blank=True)  

    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        if self.imgs:
            if os.path.isfile(self.imgs.path):
                os.remove(self.imgs.path)
        super().delete(*args, **kwargs)



# Modelo de Categoría
class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name


# Modelo de Carrito
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Cart for {self.user.username}"

    def total_price(self):
        return self.product.price * self.quantity


# Modelo de Pago
class Payment(models.Model):
    class PaymentMethod(models.TextChoices):
        CREDIT_CARD = 'CC', 'Credit Card'
        PAYPAL = 'PP', 'PayPal'
        BANK_TRANSFER = 'BT', 'Bank Transfer'

    price = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=2, choices=PaymentMethod.choices)
    date_pay = models.DateTimeField(auto_now_add=True)
    date_order = models.DateTimeField()

    def __str__(self):
        return f"Payment {self.id} for {self.price} using {self.method}"
