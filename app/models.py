from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    numero_Cel = models.CharField(max_length=50)
    direccion = models.TextField(max_length=250)
    old_cart = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = cliente(user=instance)
        user_profile.save()
    
post_save.connect(create_profile, sender=User)



class categorias(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class distribuidor(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class producto(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(categorias, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=350)
    precio = models.IntegerField()
    unid_Stock = models.CharField(max_length=50)
    vendido_por = models.CharField(max_length=50)
    enviado_por = models.ForeignKey(distribuidor, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos/", null=True)
    
    def __str__(self):
        return self.nombre

class carrito(models.Model):
    total = models.IntegerField()


class ordenes(models.Model):
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(producto, on_delete=models.CASCADE)

class direccion(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customer_direccion", null=True)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    barrio = models.CharField(max_length=50)
    calle = models.CharField(max_length=50)
    municipio_departamento = models.CharField(max_length=50)
    info_adicional = models.CharField(max_length=50)
    

