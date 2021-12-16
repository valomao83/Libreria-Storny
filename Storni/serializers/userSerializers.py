from django.contrib.auth.models import User
from rest_framework import serializers
from Storni.models.user import Usuario
from Storni.models.cuentas import Cuentas
from Storni.serializers.cuentasSerializers import CuentaSerializers

class UsuarioSerializer(serializers.ModelSerializer):
    Cuentas = CuentaSerializers()
    class Meta:
        model = Usuario
        fields = ['email', 'username', 'Password', 'Dirección de Domicilio', 'Celular', 'Fecha de Ingreso', 'Fecha de Salida','Cuentas']
 
    def crear(self, validated_data):
        accountData = validated_data.pop('cuentas')
        userInstance = Usuario.objects.create(**validated_data)
        Cuentas.objects.create(user=userInstance, **accountData)
        return userInstance

    def to_representation(self, obj):
        user = Usuario.objects.get(email=obj.email)
        account = Cuentas.objects.get(user=obj.email)
        return {
                'email': Usuario.email,
                'username': Usuario.username,
                'Direccion de Domicilio': Usuario.Dirección_Domicilio,
                'Celular': Usuario.Celular,
                'Fecha de Ingreso': Cuentas.Fecha_ingreso,
                'Fecha de Salida': Cuentas.Fecha_salida,
                'Cuentas': {
                    'email': Cuentas.email,
                    'is admin': Cuentas.is_admin,
                    'is active': Cuentas.is_active,
                    'is staff': Cuentas.is_staff,
                    'is superuser': Cuentas.is_superuser,
                }
        }
    