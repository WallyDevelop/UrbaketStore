from django.shortcuts import render, redirect, get_object_or_404
from app.models import producto, categorias, distribuidor
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def sellerdashboard(request):
    dis = distribuidor.objects.all()
    cate = categorias.objects.all()
    pro = producto.objects.all()
    return render(request, "sellerdashboard.html", {"cate":cate, "dis":dis, "pro":pro})
 
def agregarProducto(request):
    nombre = request.POST['nombreproducto']
    categoria_nombre = request.POST['categoriaproducto']
    categoria = categorias.objects.get(nombre=categoria_nombre)
    descripcion = request.POST['descripcionproducto']
    precio = request.POST['precioproducto']
    unid_Stock = request.POST['dispoproducto']
    vendido_por = request.POST['vendedor']
    enviado_por_id = request.POST['repartidor']
    enviado_por = distribuidor.objects.get(id=enviado_por_id)
    imagen = request.FILES['imagenproducto']
  
    product = producto.objects.create(
        nombre=nombre, 
        categoria=categoria, 
        descripcion=descripcion, 
        precio=precio, 
        unid_Stock=unid_Stock, 
        vendido_por=vendido_por, 
        enviado_por=enviado_por, 
        imagen=imagen
    )
    
    return redirect("/seller")

def eliminarProducto(request, pk):
    product = producto.objects.get(id=pk)
    product.delete()
    return redirect("/seller")

def editarProducto(request, pk):
    product = producto.objects.get(id=pk)
    categori = categorias.objects.all()
    distribuidors = distribuidor.objects.all() 
    return render(request, 'editar_producto.html', {"product": product, "categori":categori, "distribuidors":distribuidors})

def actualizar_Producto(request, product_id):

    nombre = request.POST['nombreproducto']
    categoria_nombre = request.POST['categoriaproducto']
    categoria = categorias.objects.get(nombre=categoria_nombre)
    descripcion = request.POST['descripcionproducto']
    precio = request.POST['precioproducto']
    unid_Stock = request.POST['dispoproducto']
    vendido_por = request.POST['vendedor']
    enviado_por_id = request.POST['repartidor']
    enviado_por = distribuidor.objects.get(id=enviado_por_id)
    if 'imagenproducto' in request.FILES:
            imagen = request.FILES['imagenproducto']
            product.imagen = imagen

    product = producto.objects.get(id=product_id)
    product.nombre = nombre
    product.categoria = categoria
    product.descripcion = descripcion
    product.precio = precio
    product.unid_Stock = unid_Stock
    product.vendido_por = vendido_por
    product.enviado_por = enviado_por
    product.imagen = imagen
    product.save()

    return redirect('/seller')

    """product = get_object_or_404(producto, id=product_id)

    if request.method == "POST":
        # Obtener los valores del formulario
        nombre = request.POST['nombreproducto']
        categoria_nombre = request.POST['categoriaproducto']
        categoria = categorias.objects.filter(nombre=categoria_nombre) 

        if not categoria:
        # Si no se encuentra la categoría, manejar el error adecuadamente
        # Esto es necesario para evitar que el campo categoría sea NULL
        # Aquí puedes redirigir a una página de error o asignar una categoría predeterminada
            return redirect('/error_categoria')

        descripcion = request.POST['descripcionproducto']
        precio = request.POST['precioproducto']
        unid_Stock = request.POST['dispoproducto']
        vendido_por = request.POST['vendedor']
        enviado_por_id = request.POST['repartidor']
        enviado_por = distribuidor.objects.get(id=enviado_por_id)

        # Manejo de la imagen: solo actualiza si se selecciona una nueva imagen
        if 'imagenproducto' in request.FILES:
            imagen = request.FILES['imagenproducto']
            product.imagen = imagen

        # Actualizar los demás campos
        product.nombre = nombre
        product.categoria = categoria
        product.descripcion = descripcion
        product.precio = precio
        product.unid_Stock = unid_Stock
        product.vendido_por = vendido_por
        product.enviado_por = enviado_por

        # Guardar el producto actualizado
        product.save()

        return redirect('/seller')  # Redirige a la página de vendedor o a donde sea necesario"""


    if request.method=="POST":
        form = UsuarioForms(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UsuarioForms()
    return render(request, "registro_vendedor.html", {"form": form})


    return render(request, "actualizar_vendedor.html")

def categoria_transportador(request):
    nombrecate = request.POST['categoria']
    nombretrans = request.POST['transportador']

    cate = categorias.objects.create(
        nombrecate = nombrecate
    )

    trans = distribuidor.objects.create(
        nombretrans = nombretrans
    )
