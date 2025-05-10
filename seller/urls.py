from django.urls import path
from . import views

urlpatterns = [
    path('', views.sellerdashboard, name="selldash"),
    path('agregarProducto/', views.agregarProducto),
    path('eliminarProducto/<int:pk>/', views.eliminarProducto),
    path('editarProducto/<int:pk>', views.editarProducto),
    path('actualizarProducto/<int:product_id>', views.actualizar_Producto, name='actualizar_producto'),
    path('registrovendedor/', views.registro_vendedor, name='registro_vendedor'),
    path('ingresovendedor/', views.ingreso_vendedor, name='ingreso_vendedor'),
    path('actualizarvendedor/', views.actualizar_vendedor, name='actualizar_vendedor'),
    path('actualizarte/', views.actualizarte, name='actualizarte'),
    path('contraseñavendedor/', views.contrasena_vendedor, name='contrasena_vendedor'),
    
    
    
]