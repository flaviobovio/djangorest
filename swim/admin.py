""" register models in admin panel """
from django.contrib import admin
from .models import Club, Swimmer, Date, Mark, Category

# Register your models here.
admin.site.register(Club)
admin.site.register(Category)
admin.site.register(Swimmer)
admin.site.register(Date)
admin.site.register(Mark)

