from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import *
from rest_framework import routers

# Configuracion API
router = routers.DefaultRouter()
router.register('tipoempleados', TipoEmpleadoViewset)
router.register('empleados', EmpleadoViewset)
router.register('servicios', ServicioViewset)


urlpatterns = [
    # Index
    path('', index, name="index"),
    # Empleados
    path('empleados/', empleados, name="empleados"),
    path('empleados/add/', empleadosadd, name="empleadosadd"),
    path('empleados/crud/update/<id>/', empleadosupdate, name="empleadosupdate"),
    path('empleados/crud/delete/<id>/', empleadosdelete, name="empleadosdelete"),
    # Servicios
    path('servicios/', servicios_principal, name="servicios"),
    path('servicios/add/', serviciosadd, name="serviciosadd"),
    path('servicios/crud/update/<id>/', serviciosupdate, name="serviciosupdate"),
    path('servicios/crud/delete/<id>/', serviciosdelete, name="serviciosdelete"),
    path('servicios/tipo/general/', general, name="general"),
    path('servicios/tipo/electrico/', electrico, name="electrico"),
    path('servicios/tipo/frenos/', frenos, name="frenos"),
    path('servicios/tipo/motriz/', motriz, name="motriz"),
    # Registro
    path('register/', register, name="register"),
    path('custom_logout/', custom_logout, name='custom_logout'),
    # Cuentas
    path('account_lock/', account_lock, name="account_lock"),
    # API
    path('api/', include(router.urls)),
    path('empleadosapi/', empleadosapi, name="empleadosapi"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)