from django.db import models

# Create your models here.
class seller(models.Model):
    nombre_empresa = models.OneToOneField
    imagen_logo = models.ImageField
    email = models.EmailField
    phone = models.IntegerField
    address = models.TextField(max_length=100)
