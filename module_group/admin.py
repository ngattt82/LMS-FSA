from django.contrib import admin

# Register your models here.
from .models import ModuleGroup, Module

admin.site.register(ModuleGroup)
admin.site.register(Module)
