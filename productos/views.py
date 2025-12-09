from django.shortcuts import render, get_object_or_404
from .models import Producto
from .forms import ProductoForm

def index(request):
  productos = Producto.objects.select_related('categoria').all()
  print(productos)
  return render(request, 'index.html', context={'productos': productos})

def detalle(request, producto_id):
  producto = get_object_or_404(Producto, id=producto_id)
  return render(request, 'detalle.html', context={'producto': producto})

def formulario(request):
  form = ProductoForm()
  return render(request, 'formulario.html', context={'form': form})