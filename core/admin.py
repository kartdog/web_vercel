from django.contrib import admin
from .models import *
from admin_confirm import AdminConfirmMixin
from django.contrib.admin import ModelAdmin

class TipoEmpleadoModelAdmin(AdminConfirmMixin, ModelAdmin):
    confirm_change = True
    confirmation_fields = ['descripcion']

class EmpleadoModelAdmin(AdminConfirmMixin, ModelAdmin):
    confirm_change = True
    confirmation_fields = ['rut','nombre','apellido','descripcion','imagen']

class ServicioModelAdmin(AdminConfirmMixin, ModelAdmin):
    confirm_change = True
    confirmation_fields = ['nombre_servicio','descripcion_servicio','pagina_servicio','costo_servicio','imagen_servicio']

# Register your models here.

admin.site.register(TipoEmpleado, TipoEmpleadoModelAdmin)
admin.site.register(Empleado, EmpleadoModelAdmin)
admin.site.register(Servicio, ServicioModelAdmin)
