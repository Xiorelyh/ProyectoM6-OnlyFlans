from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Flan, ContactForm
from .forms import ContactFormForm
from django.contrib import messages

# Vista principal que carga todos los flanes
def indice(request):
    flans = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flans': flans})

def acerca(request):
    return render(request, 'about.html', {})

def bienvenido(request):
    flans = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'flans': flans})

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