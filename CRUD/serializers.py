from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Vehiculo, Conductor, Pasajero, Arrendamiento

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password'
        ]
class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'

class ConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conductor
        fields = '__all__'

class PasajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pasajero
        fields = '__all__'

class ArrendamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arrendamiento
        fields = '__all__'
