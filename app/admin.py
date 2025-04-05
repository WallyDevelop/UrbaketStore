from django.contrib import admin
from .models import carrito, producto, cliente, ordenes, categorias, direccion, distribuidor
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(carrito)
admin.site.register(producto)
admin.site.register(ordenes)
admin.site.register(categorias)
admin.site.register(direccion)
admin.site.register(distribuidor)
admin.site.register(cliente)

#Mezclamos informacion de cliente y usuarios
class ProfileInLine(admin.StackedInline):
    model = cliente

#Extendemos el model de usuario
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username", "first_name", "last_name", "email"]
    inlines = [ProfileInLine]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)