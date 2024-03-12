""" register models in admin panel """
from django.contrib import admin
from .models import Swimmer

# Register your models here.
admin.site.register(Swimmer)
