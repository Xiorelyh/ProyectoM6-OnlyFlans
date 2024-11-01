from django import forms
from .models import ContactForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Formulario de Contacto
class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label="Correo")
    customer_name = forms.CharField(max_length=64, label="Nombre")
    message = forms.CharField(label="Mensaje")


class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ["customer_email", "customer_name", "message"]

#Formulario Registro de Usuario
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')