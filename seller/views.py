from django.shortcuts import render, redirect
from app.models import producto, categorias, distribuidor
from .models import seller

# Create your views here.
def sellerdashboard(request):
    dis = distribuidor.objects.all()
    cate = categorias.objects.all()
    vendedor = request.user
    pro= producto.objects.all()
    return render(request, "sellerdashboard.html", {"pro":pro, "cate":cate, "dis":dis})
 
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

def editarProducto(request):
    pass