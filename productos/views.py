from django.shortcuts import render
from .models import Producto

def index(request):
  productos = Producto.objects.select_related('categoria').all()
  print(productos)
  return render(request, 'index.html', context={'productos': productos})