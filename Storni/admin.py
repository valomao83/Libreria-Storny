from django.contrib import admin
from .models.user import Usuario
from .models.cuentas import Cuentas

admin.site.register(Usuario)
admin.site.register(Cuentas)

# Register your models here.
