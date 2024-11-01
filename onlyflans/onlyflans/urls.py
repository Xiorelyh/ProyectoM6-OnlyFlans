"""
URL configuration for onlyflans project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from web import views
from django.contrib.auth import views as auth_views
from web.views import BienvenidoView, iniciar_sesion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indice, name="indice"),
    path('acerca', views.acerca, name="acerca"),
    path('bienvenido/', BienvenidoView.as_view(), name='bienvenido'),
    path('contacto', views.contacto, name="contacto"),
    path('registro/', views.registro, name="registro"),
    path('accounts/login/', iniciar_sesion, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('accounts/', include('django.contrib.auth.urls')), 
]
