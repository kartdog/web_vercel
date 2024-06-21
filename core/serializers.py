from rest_framework import serializers
from .models import *

# TRANSFORMA PYTHON A JSON

class TipoEmpleadoSerializers(serializers.ModelSerializer):
    
    class Meta: 
            model = TipoEmpleado
            fields = '__all__'

class EmpleadoSerializers(serializers.ModelSerializer):
    tipo = TipoEmpleadoSerializers(read_only=True)

    class Meta: 
            model = Empleado
            fields = '__all__'

class ServicioSerializers(serializers.ModelSerializer):
    
    class Meta: 
            model = Servicio
            fields = '__all__'