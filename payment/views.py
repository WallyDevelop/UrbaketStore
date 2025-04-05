from django.shortcuts import render
from cart.cart import Cart
from app.models import direccion
# Create your views here.
def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals= cart.cart_total()
    cliente = request.user
    usuario = direccion.objects.filter(cliente=cliente)
    return render(request, "payment/checkout.html", {"cart_products": cart_products, "quantities": quantities, "totals":totals, "usuario": usuario})
    

def payment_success(request):
    return render(request, "payment/payment_success.html")

