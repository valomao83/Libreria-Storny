from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.db.models.signals import post_save
from django.conf import settings

# Create your models here.

class GestiondeUsuarios (BaseUserManager):
    
    def Crear_Usuario(self,email,username,password=None):
        if  not email:
            raise ValueError("El ususario debe indicar un correo electronico válido")
        if not username:
            raise ValueError("EL usuario debe contar con un username")
    
        User = self.model(
            email=email,
            username=username,
        )

        User.set_password(password)
        User.save(using=self._db)
        return User

    def Crear_Superusuario(self, email, username, password):
        User=self.Crear_Usuario(
            email=email,
            password=password,
            username=username,
        )
        User.is_admin = True
        User.is_staff = True
        User.is_Superusuario = True
        User.save(using=self._db)
        return User

class Usuario(AbstractBaseUser):
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=100)
    Fecha_ingreso = models.DateTimeField(verbose_name='Fecha de Ingreso', auto_now_add=True)
    Fecha_salida = models.DateTimeField(verbose_name='Fecha de Salida', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    Dirección_Domicilio = models.CharField(max_length=300)
    Celular = models.CharField(max_length=15, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['username']

    objects = GestiondeUsuarios()

    def __str__(self):
        return self.username

    def has_perm(self,per,obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

