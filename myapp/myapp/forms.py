from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioDoctor(forms.Form):
    usuario = forms.CharField(max_length=30)
    nombre=forms.CharField()
    apellido= forms.CharField()
    dni=forms.CharField()
    area= forms.CharField()
    

class FormularioPaciente(forms.Form):
    
    usuario = forms.CharField(max_length=30)
    nombre=forms.CharField()
    apellido=forms.CharField()
    dni=forms.CharField()
    obraSocial=forms.CharField()

class FormularioTurno(forms.Form):
    usuario = forms.CharField(max_length=30)
    paciente=forms.CharField()
    fecha=forms.CharField()
    dni=forms.CharField()
    especial=forms.CharField()

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repetir Contraseña ',widget=forms.PasswordInput)

    class Meta:
        model= User
        fields=['username','email','password1','password2']
        help_texts={k:"" for k in fields}

class UserEditForm(UserCreationForm):
        email = forms.EmailField(label="Ingrese su email:")
        password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
        password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

        last_name = forms.CharField()
        first_name = forms.CharField()

        class Meta:
            model = User
            fields = ['email', 'password1', 'password2', 'last_name', 'first_name']
            help_texts = {k:"" for k in fields}
