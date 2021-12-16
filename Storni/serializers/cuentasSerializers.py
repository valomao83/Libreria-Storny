from Storni.models.cuentas import Cuentas
from rest_framework import serializers

class CuentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuentas
        fields = ['is admin', 'is active', 'is staff', 'is superuser']