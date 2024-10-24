from django import forms
from .models import Vehiculo

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio']
        labels = {
            'marca': 'Marca',
            'modelo': 'Modelo',
            'serial_carroceria': 'Serial Carroceria',
            'serial_motor': 'Serial Motor',
            'categoria': 'Categoría',
            'precio': 'Precio',
            }
            
