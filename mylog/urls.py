# mylog/urls.py

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = 'mylog'

urlpatterns = [
    path('', views.home, name='home'),
    path('log/', views.login_register_view, name='login_register'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.custom_logout, name='logout'),
    path('addproduct/', views.addProduct, name='addproduct'),
    path('userp/<str:name>/', views.userP, name="userProfile"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)