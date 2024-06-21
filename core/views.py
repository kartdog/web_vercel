from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from .serializers import *
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from django.core.paginator import Paginator
import requests

# Vistas
def electrico(request):
    return render(request, 'core/servicios/tipo/electrico.html')

def frenos(request):
    return render(request, 'core/servicios/tipo/frenos.html')

def general(request):
    return render(request, 'core/servicios/tipo/general.html')

def motriz(request):
    return render(request, 'core/servicios/tipo/motriz.html')

def register(request):
    return render(request, 'registration/register.html')

def account_lock(request):
    return render(request, 'core/account_lock.html')

def custom_logout(request):
    logout(request)
    return redirect('index')

def index(request):
    servicios = Servicio.objects.all()
    empleados = Empleado.objects.all()
    
    contexto = {
        'lista_servicios': servicios,
        'lista_empleados': empleados
    }

    return render(request, 'core/index.html', contexto)

# Funciones
# Funcion, empleado.
def empleados(request):
    empleados = Empleado.objects.all() # SELECT * FROM empleado
    aux = {
        'lista' : empleados
    }

    return render(request, 'core/empleados/index.html', aux)

@permission_required('core.add_empleado')
def empleadosadd(request):
    aux = {
            'form' : EmpleadoForm()
    }

    if request.method == 'POST':
        formulario = EmpleadoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            aux['msj'] = 'Empleado almacenado correctamente!'
            return redirect('empleados')
        else:
            aux['form'] = formulario
            aux['msj'] = 'No se pudo almacenar :('

    return render(request, 'core/empleados/crud/add.html', aux)

@permission_required('core.change_empleado')
def empleadosupdate(request, id):
    empleado = Empleado.objects.get(id=id)
    aux = {
            'form' : EmpleadoForm(instance = empleado)
    }

    if request.method == 'POST':
        formulario = EmpleadoForm(data = request.POST, instance = empleado, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            aux['msj'] = 'Empleado modificado correctamente!'
            return redirect('empleados')
        else:
            aux['form'] = formulario
            aux['msj'] = 'No se pudo modificar :('

    return render(request, 'core/empleados/crud/update.html', aux)

@permission_required('core.delete_empleado')
def empleadosdelete(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()

    return redirect(to="empleados")

# Funcion, servicios.
def servicios_principal(request):
    servicios = Servicio.objects.all()
    aux = {
        'lista' : servicios
    }

    return render(request, 'core/servicios/index.html', aux)

def servicios_general(request):
    servicios = Servicio.objects.all()
    aux = {
        'lista' : servicios
    }

    return render(request, 'core/index.html', aux)

@login_required
def serviciosadd(request):
    aux = {
            'form' : ServicioForm()
    }

    if request.method == 'POST':
        formulario = ServicioForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            aux['msj'] = 'Empleado almacenado correctamente!'
            return redirect('servicios')
        else:
            aux['form'] = formulario
            aux['msj'] = 'No se pudo almacenar :('

    return render(request, 'core/servicios/crud/add.html', aux)

@permission_required('core.change_servicio')
def serviciosupdate(request, id):
    servicio = Servicio.objects.get(id=id)
    aux = {
            'form' : ServicioForm(instance = servicio)
    }

    if request.method == 'POST':
        formulario = ServicioForm(data = request.POST, instance = servicio, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            aux['msj'] = 'Servicio modificado correctamente!'
            return redirect('servicios')
        else:
            aux['form'] = formulario
            aux['msj'] = 'No se pudo modificar :('

    return render(request, 'core/servicios/crud/update.html', aux)

@permission_required('core.delete_servicio')
def serviciosdelete(request, id):
    servicio = Servicio.objects.get(id=id)
    servicio.delete()

    return redirect(to="servicios")

# Funcion, registrar.
def register(request):
    aux = {
        'form' : UserCreation()
    }

    if request.method == 'POST':
        formulario = UserCreation(request.POST)
        if formulario.is_valid():
            user = formulario.save()
            group = Group.objects.get(name = 'cliente')
            user.groups.add(group)
            #aux['msj'] = 'Empleado almacenado correctamente!'
            user = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password2'])
            login(request, user)
            return redirect(to='index')
        else:
            aux['form'] = formulario
            aux['msj'] = 'No se pudo almacenar :('

    return render(request, 'registration/register.html', aux)

# Serializers.
class TipoEmpleadoViewset(viewsets.ModelViewSet):
    queryset = TipoEmpleado.objects.all()
    serializer_class = TipoEmpleadoSerializers
    renderer_classes = [JSONRenderer]

class EmpleadoViewset(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializers
    renderer_classes = [JSONRenderer]

class ServicioViewset(viewsets.ModelViewSet):

    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializers
    renderer_classes = [JSONRenderer]

# API.
def empleadosapi(request):
    response = requests.get('http://127.0.0.1:8000/api/empleados/')
    empleados = response.json()

    # Paginator
    paginator = Paginator(empleados, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    aux = {
        'lista' : empleados
    }

    return render(request, 'core/empleados/crud_api/index.html', aux)