from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.db.models.base import Model
from django.forms import fields
from django.forms.models import _Labels
from Storni.models import cuentas

class Forma_de_Resgistro(UserCreationForm):
    password1= forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2= forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        Model = cuentas
        fields = ('email', 'username', 'password1', 'password2')
        _Labels = {'username': 'Nombre Completo', 'email': 'Ingresa un correo electronico'}

class Autenticar_Forma(forms.ModelForm):

    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = cuentas
        fields = ('email', 'password')
    
    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError("El mail o la contraseña son incorrectas")
        