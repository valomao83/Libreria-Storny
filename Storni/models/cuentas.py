from django.db import models
from .user import User

class Cuentas(models.Model):
    email = models.EmailField(max_length=50, unique=True)
    User = models.ForeignKey(User,related_name='Cuenta', on_delete=models.CASCADE)
    Fecha_ingreso = models.DateTimeField(verbose_name='Fecha de Ingreso', auto_now_add=True)
    Fecha_salida = models.DateTimeField(verbose_name='Fecha de Salida', auto_now=True)
    is_active = models.BooleanField(default=True)
    