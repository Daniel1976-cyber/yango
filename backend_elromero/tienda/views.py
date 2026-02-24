from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from .forms import ProductoForm
from .models import Producto

@staff_member_required
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto agregado exitosamente')
            return redirect('agregar_producto')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario')
    else:
        form = ProductoForm()
    
    productos = Producto.objects.all()
    return render(request, 'tienda/agregar_producto.html', {
        'form': form,
        'productos': productos
    })

@staff_member_required
def editar_producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado exitosamente')
            return redirect('agregar_producto')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario')
    else:
        form = ProductoForm(instance=producto)
    
    productos = Producto.objects.all()
    return render(request, 'tienda/agregar_producto.html', {
        'form': form,
        'productos': productos,
        'producto_editar': producto
    })

@staff_member_required
def cambiar_estado_producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    producto.activo = not producto.activo
    producto.save()
    estado = "activado" if producto.activo else "desactivado"
    messages.success(request, f'Producto {producto.nombre} {estado} exitosamente')
    return redirect('agregar_producto')

def tienda(request):
    return render(request, 'tienda/bazarelromero.html')
