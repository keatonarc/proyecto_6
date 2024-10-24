from django.shortcuts import render, redirect
from .forms import VehiculoForm
from .models import Vehiculo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required



# Create your views here.
def index(request):
    return render(request, 'index.html')

# Decoradores de permisos
@permission_required('vehiculo.vehiculo_add')  # Asegúrate de que el permiso es correcto
def agregar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/vehiculo_add.html', {'form': form})


@login_required  # usuarios autenticados puedan acceder
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()  # Obtiene todos los vehículos

    # Clasifica los vehículos por precio
    precios = []
    for vehiculo in vehiculos:
        if vehiculo.precio < 10000:
            precios.append((vehiculo, 'Bajo'))
        elif 10000 <= vehiculo.precio <= 30000:
            precios.append((vehiculo, 'Medio'))
        else:
            precios.append((vehiculo, 'Alto'))

    return render(request, 'vehiculo/listar.html', {'precios': precios})




