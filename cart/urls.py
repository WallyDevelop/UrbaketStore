from django.urls import path
from . import views

urlpatterns = [
    path('', views.resumen_carrito, name="cart_detail"),
    path('agregar/', views.cart_add, name="cart_add"),
    path('delete/', views.cart_delete, name="cart_delete"),
    path('update/', views.cart_decrement, name="cart_update"),
    
]
