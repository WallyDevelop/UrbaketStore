from django.shortcuts import render, redirect, get_object_or_404
from app.models import producto, categorias, distribuidor
from .models import seller
from django.contrib.auth import authenticate, login, logout
from django import forms 
from .forms import SellerRegistrationForm, ChangePasswordSeller, UpdateUserFormSeller
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

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

def registro_vendedor(request):
    registroseller = SellerRegistrationForm()
    if request.method=="POST":
        registroseller = SellerRegistrationForm(request.POST)
        if registroseller.is_valid():
            registroseller.save()
            username = registroseller.cleaned_data["username"]
            password = registroseller.cleaned_data["password1"]
            # Ingresamos
            user = authenticate(username=username, password=password)
            login(request, user)
            return render(request, 'sellerdashboard.html')
    else:
        return render(request, "registro_vendedor.html", {"registroseller": registroseller})
    
def ingreso_vendedor(request):
    if request.method == 'GET':
        return render(request, 'ingreso_vendedor.html', {'ingresovendedorform': AuthenticationForm})
    else:
        user=authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return redirect('registro_vendedor')
        else:
            login(request,user)
            return render(request, "sellerdashboard.html")

def actualizarte(request):
    return render(request, "actualizar_vendedor.html")

def actualizar_vendedor(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        actsellform = UpdateUserFormSeller(request.POST or None, instance=current_user)

        if actsellform.is_valid():
            actsellform.save()
            
            login(request, current_user)
            return redirect('selldash')
        return render (request, "actualizar_vendedor.html", {"actsellform": actsellform})
    else:
        return redirect('selldash')


def contrasena_vendedor(request):
    pass