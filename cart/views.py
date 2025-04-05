from django.shortcuts import render, get_object_or_404, redirect
from app.models import producto
from .cart import Cart
from django.http import JsonResponse


# Create your views here.
def resumen_carrito(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals= cart.cart_total()
    return render(request, "resumen_carrito.html", {"cart_products": cart_products, "quantities": quantities, "totals":totals})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(producto, id=product_id)
        cart.add(product=product, quantity=product_qty)
        cart_quantity = cart.__len__()
        response = JsonResponse({'qty': cart_quantity})
        return response


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        response = JsonResponse({"product": product_id})
        return response 


def cart_decrement(request):
    pass


def cart_clear(request):
    pass
