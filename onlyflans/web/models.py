import uuid
from django.db import models
from django.utils.text import slugify

# Create your models here.

class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=64, blank=False)
    description = models.TextField(blank=False, null=False)
    image_url = models.URLField(blank=False)
    slug = models.SlugField(unique=True, max_length=255, blank=True)
    is_private = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name


class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer_email = models.EmailField(blank=False)
    customer_name = models.CharField(max_length=64, blank=False)
    message = models.TextField(blank=False)

    def __str__(self):
        return f"{self.customer_name} - {self.customer_email}"