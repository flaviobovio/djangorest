""" register models in admin panel """
from django.contrib import admin
from .models import Swimmer, Date, Mark

# Register your models here.
admin.site.register(Swimmer)
admin.site.register(Date)
admin.site.register(Mark)
