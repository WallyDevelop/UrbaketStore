from django.shortcuts import render, HttpResponse

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import producto, direccion, cliente
from django import forms 
from .forms import SignUpForm, UpdateUserForm, ChangePassword
import json
from cart.cart import Cart


# Create your views here.
def registrarse(request):
    registroform = SignUpForm()
    if request.method=="POST":
        registroform = SignUpForm(request.POST)
        if registroform.is_valid():
            registroform.save()
            username = registroform.cleaned_data["username"]
            password = registroform.cleaned_data["password1"]
            # Ingresamos
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('inicio')
    else:
        return render(request, 'registro.html', {'registroform' : registroform})

def actualizar_usuario(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        actform = UpdateUserForm(request.POST or None, instance=current_user)

        if actform.is_valid():
            actform.save()
            
            login(request, current_user)
            return redirect('inicio')
        return render (request, "actualizar_user.html", {"actform": actform})
    else:
        return redirect('inicio')

def actualizar_pass(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method=='POST':
            contraform =ChangePassword(current_user, request.POST)
            if contraform.is_valid():
                contraform.save()
                login(request, current_user)
                return redirect('inicio')
            else:
                for error in list(contraform.errors.values()):
                    pass
        else:
            contraform = ChangePassword(current_user)
            return render(request, 'actualizar_pass.html', {'contraform':contraform})
    else:
        return redirect('inicio')
    
def ingresar(request):
    if request.method == 'GET':
        return render(request, 'ingresar.html', {'ingresoform': AuthenticationForm})
    else:
        user=authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return redirect('registrarse')
        else:
            login(request,user)
            
            current_user = cliente.objects.get(user__id = request.user.id)
            saved_cart = current_user.old_cart
            if saved_cart:
                converted_cart = json.loads(saved_cart)
                cart = Cart(request)
                for key, value in converted_cart.items(): # Cuando recorremos un diccionario en Python agregamos el .items()
                    cart.db_add(product=key, quantity=value)

            return redirect('inicio')

def salir(request):
    logout(request)
    return redirect('inicio')

def index(request):
    products = producto.objects.all()
    return render(request, 'index.html', {"product":products})

def detallesproducto(request, pk):
    detalleProducto = producto.objects.get(id=pk)
    return render(request, "detalles_productos.html", {"detallePro":detalleProducto})

def cuenta(request):
    return render(request, "cuenta.html")

def actualizarcuenta(request):
    return render(request, "actualizarCuenta.html", {"actualizarform":UserChangeForm})

def direcciones(request):
    cliente = request.user
    usuario = direccion.objects.filter(cliente=cliente)
    return render(request, "direccionBook.html", {"usuario":usuario})

def agregardireccion(request):
    cliente = request.user 
    nombre = request.POST['nombrecompleto']
    telefono = request.POST['telefono']
    barrio = request.POST['barrio']
    calle = request.POST['info']
    municipio_departamento = request.POST['municipio']
    info_adicional = request.POST['infoadicional']

    direc = direccion.objects.create(
        cliente=cliente, 
        nombre=nombre, 
        telefono=telefono, 
        barrio=barrio, 
        calle=calle, 
        municipio_departamento=municipio_departamento, 
        info_adicional=info_adicional
        )

    return redirect('direccion')

def ediciondireccion(request, pk):
    direc = direccion.objects.get(id=pk)
    return render(request, "editardireccion.html", {"direc":direc})

def editardireccion(request, pk):
    nombre = request.POST['nombrecompleto']
    telefono = request.POST['telefono']
    barrio = request.POST['barrio']
    calle = request.POST['info']
    municipio_departamento = request.POST['municipio']
    info_adicional = request.POST['infoadicional']

    direcc = direccion.objects.get(id=pk)
    direcc.nombre = nombre
    direcc.telefono = telefono
    direcc.barrio = barrio
    direcc.calle = calle
    direcc.municipio_departamento = municipio_departamento
    direcc.info_adicional = info_adicional

    direcc.save()

    cliente = request.user
    usuario = direccion.objects.filter(cliente=cliente)
    return render(request, "direccionBook.html", {"usuario":usuario})

def eliminardireccion(request, pk):
    direcc = direccion.objects.get(id=pk)
    direcc.delete()

    cliente = request.user
    usuario = direccion.objects.filter(cliente=cliente)
    return render(request, "direccionBook.html", {"usuario":usuario})

def pagos(request):
    return render(request, "pagos.html")

def ordenes(request):
    return render(request, "ordenes.html")

def acerca_de(request):
    return render(request, "acerca_de.html")

def vende_nosotros(request):
    return render(request, "vende_nosotros.html")

def buscar(request):
    if request.method == "POST":
        searched = request.POST["buscar"]
        searched = producto.objects.filter(nombre__icontains=searched)
        return render(request, "buscar.html", {'searched':searched})
    else:
        return render(request, "buscar.html", {'searched':searched})