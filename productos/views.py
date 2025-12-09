from django.shortcuts import render, get_object_or_404
from .models import Producto
from .forms import ProductoForm
from django.http import HttpResponseRedirect

def index(request):
  productos = Producto.objects.select_related('categoria').all()
  print(productos)
  return render(request, 'index.html', context={'productos': productos})

def detalle(request, producto_id):
  producto = get_object_or_404(Producto, id=producto_id)
  return render(request, 'detalle.html', context={'producto': producto})

def formulario(request):
  if request.method == 'POST':
    form = ProductoForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/productos')
  else:
    form = ProductoForm()

  return render(request, 'formulario.html', context={'form': form})