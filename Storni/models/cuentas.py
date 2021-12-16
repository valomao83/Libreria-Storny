from django.db import models
from .user import User

class Cuentas(models.Model):
    email = models.EmailField(max_length=50, unique=True)
    User = models.ForeignKey(User,related_name='Cuenta', on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    