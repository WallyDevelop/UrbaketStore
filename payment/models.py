from django.db import models
from app.models import producto
from django.contrib.auth.models import User

# Create your models here.
class order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null= True, blank=True)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    shipping_addess = models.TextField(max_length=15000)
    amount_paid = models.DecimalField(max_digits=30, decimal_places=2)
    date_ordered = models.DateField(auto_now=True)

    def __str__(self):
        return f'"order - {str(self.id)}'

class orderItem(models.Model):
    order = models.ForeignKey(order, on_delete=models.CASCADE, null= True)
    product = models.ForeignKey(producto, on_delete=models.CASCADE, null= True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null= True, blank=True)

    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(max_digits=30, decimal_places=2)

    def __str__(self):
        return f'Articulo Ordenado - {str(self.id)}'



