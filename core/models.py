from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class TipoEmpleado(models.Model):
    descripcion = models.CharField(max_length=40)

    def __str__(self):
        return self.descripcion
    
class Empleado(models.Model):

    OPCIONES = [
        ('---', '---'),
        ('general', 'general'),
        ('electrico', 'electrico'),
        ('motriz', 'motriz'),
        ('frenos', 'frenos'),
    ]

    OPCION_DEFAULT = '---'

    rut = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_ingreso = models.DateTimeField(auto_now_add = True)
    tipo = models.ForeignKey(TipoEmpleado, on_delete = models.CASCADE)
    tipo_mecanico = models.CharField(max_length=20, choices=OPCIONES, default=OPCION_DEFAULT)
    descripcion = models.TextField(max_length=550)
    imagen = CloudinaryField('imagen')

    def __str__(self):
        return self.rut
    
class Servicio(models.Model):
    nombre_servicio = models.CharField(max_length=200)
    descripcion_servicio = models.TextField(max_length=550)
    costo_servicio = models.CharField(max_length=100)
    pagina_servicio = models.CharField(max_length=500)
    imagen_servicio = CloudinaryField('imagen')

    def __str__(self):
        return self.nombre_servicio
    
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=64)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre_producto