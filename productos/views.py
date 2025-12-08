from django.shortcuts import render
from .models import Producto

def index(request):
  productos = Producto.objects.select_related('categoria').all()
  print(productos)
  return render(request, 'index.html', context={'productos': productos})

def detalle(request, producto_id):
  producto = Producto.objects.select_related('categoria').get(id=producto_id)
  return render(request, 'detalle.html', context={'producto': producto})