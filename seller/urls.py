from django.urls import path
from . import views

urlpatterns = [
    path('', views.sellerdashboard, name="selldash"),
    path('agregarProducto/', views.agregarProducto),
    path('eliminarProducto/<int:pk>/', views.eliminarProducto),
    path('editarProducto/<int:pk>', views.editarProducto),
    path('actualizarProducto/<int:product_id>', views.actualizar_Producto, name='actualizar_producto'),
    path('agregarDatos/', views.categoria_transportador, name='cateytranspo'),
    path('vercateytranspo/', views.cateytrans)
  
]