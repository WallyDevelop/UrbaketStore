from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="inicio"),
    path('registro/', views.registrarse, name="registrarse"),
    path('actualizar_usuario/', views.actualizar_usuario, name='act_user'),
    path('actualizar_contrasena/', views.actualizar_pass, name='act_pass'),
    path('inicio-sesion/', views.ingresar, name="ingresar" ),
    path('cerrar-sesion/', views.salir, name="salir"),
    path('detalle_producto/<int:pk>', views.detallesproducto, name='detalle'),
    path('configuracion_cuenta/', views.cuenta, name="cuenta"),
    path('actualizar_cuenta/',views.actualizarcuenta, name="actualizar"),
    path('direcciones/',views.direcciones, name="direccion"),
    path('metodos_pago/', views.pagos, name='pagos'),
    path('ordenes/',views.ordenes, name="ordenes"),
    path('agregardireccion/', views.agregardireccion, name="add_direction"),
    path('ediciondireccion/<int:pk>', views.ediciondireccion, name="editardir"),
    path('editardireccion/<int:pk>', views.editardireccion),
    path('eliminardireccion/<int:pk>', views.eliminardireccion, name="eliminardireccion"),
    path('acerca_de/', views.acerca_de, name="acerca"),
    path('vende_nosotros/', views.vende_nosotros, name="vende")
]
