from django.db import models
from django.contrib.auth.models import Permission
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.
class Vehiculo(models.Model):
    MARCAS = [
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota')
    ]
    CATEGORIAS = [
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    ]
    
    marca = models.CharField(max_length=20, choices=MARCAS, default='Ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='Particular')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = [
            ('visualizar_catalogo', 'Puede visualizar Catálogo de Vehículos'),
            ('agregar_vehiculo', 'Puede agregar Vehículos'),
        ]


    def __str__(self):
        return f"{self.marca} {self.modelo}"
    
    # Crear el permiso
@receiver(post_save, sender=User)
def assign_view_catalog_permission(sender, instance, created, **kwargs):
    if created:
        permission = Permission.objects.get(codename='visualizar_catalogo')
        instance.user_permissions.add(permission)
        