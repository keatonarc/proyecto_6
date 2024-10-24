from django.contrib import admin
from .models import Vehiculo
# Register your models here.

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio', 'fecha_creacion', 'fecha_modificacion')
    search_fields = ('marca', 'modelo', 'serial_carroceria', 'serial_motor', 'precio')
    list_filter = ('marca', 'modelo', 'serial_carroceria', 'serial_motor')