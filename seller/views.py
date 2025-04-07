from django.shortcuts import render
from app.models import producto
from .models import seller

# Create your views here.
def sellerdashboard(request):
    vendedor = request.user
    pro= producto.objects.all()
    return render(request, "sellerdashboard.html", {"pro":pro})
 