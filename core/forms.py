from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Invisible


class EmpleadoForm(ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Empleado
        fields = '__all__'

class TipoEmpleadoForm(ModelForm):

    class Meta:
        model = TipoEmpleado
        fields = '__all__'

class ServicioForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Servicio
        fields = '__all__'

class UserCreation(UserCreationForm):
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ['username','password1','password2']