# myauth/urls.py (archivo de URLs principal)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mylog.urls', namespace='mylog')),  # Agregamos el namespace aquí
]