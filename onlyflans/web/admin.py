from django.contrib import admin
from .models import Flan
from .models import ContactForm

# Register your models here.

@admin.register(Flan)
class FlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_private')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(ContactForm)

