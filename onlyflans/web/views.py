from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView
from .models import Flan, ContactForm
from .forms import ContactFormForm
from .forms import RegistroForm
from django.urls import path


# Vista principal que carga todos los flanes
def indice(request):
    flans = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flans': flans})


def acerca(request):
    return render(request, 'about.html', {})


# Vista Pantalla Bienvenida Mostrando nombre de usuario. 
@method_decorator(login_required, name='dispatch')
class BienvenidoView(TemplateView):
    template_name = 'welcome.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre_usuario'] = self.request.user.username 
        context['flans'] = Flan.objects.filter(is_private=True)
        return context


# Vista de Contacto
def contacto(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            messages.success(request, "Gracias por contactarte con OnlyFlans. Te responderemos en breve.")
            form = ContactFormForm()  
    
    else:
        form = ContactFormForm()

    return render(request, 'contacto.html', {'form': form})


# Vistas de Registro

@require_http_methods(["GET", "POST"])
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario registrado exitosamente.")
            return redirect('bienvenido')  # Redirige a la página de bienvenida o a la página que desees
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})


# Vistas de Login
def iniciar_sesion(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('bienvenido')  
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
    return render(request, 'registration/login.html')