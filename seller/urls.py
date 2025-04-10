from django.urls import path
from . import views

urlpatterns = [
    path('', views.sellerdashboard, name="selldash"),
    path('agregarProducto/', views.agregarProducto),
    path('eliminarProducto/<int:pk>/', views.eliminarProducto),
    path('editarProducto/', views.editarProducto),
    
    
]