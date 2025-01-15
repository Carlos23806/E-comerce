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
    path('profile/', views.profile_view, name='profile'),
    path('profile/info/', views.user_info, name='user_info'),
    path('profile/products/', views.user_products, name='user_products'),
    path('profile/update/', views.update_user, name='update_user'),
    path('profile/products/edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('profile/products/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('cart/', views.cart_view, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/', views.update_cart, name='update_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)