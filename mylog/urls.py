# mylog/urls.py

from django.urls import path
from . import views

app_name = 'mylog'  # Definimos el app_name aquí

urlpatterns = [
    path('', views.home, name='home'),
    path('log/', views.login_register_view, name='login_register'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]