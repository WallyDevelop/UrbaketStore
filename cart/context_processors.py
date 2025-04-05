from .cart import Cart

# Creamos el contexto del procesor que trabaje en todas las paginas
def cart(request):
    # Retornamos los datos por defecto del carrito
    return{"cart":Cart(request)}