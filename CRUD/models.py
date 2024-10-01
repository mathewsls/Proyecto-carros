# models.py
from django.db import models

class Vehiculo(models.Model):
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    placa = models.CharField(max_length=10)
    fecha_fabricacion = models.DateTimeField()
    fecha_inicial_soat = models.DateTimeField()
    fecha_final_soat = models.DateTimeField()
    is_active = models.BooleanField(default=True)

class Conductor(models.Model):
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    cedula = models.IntegerField()
    correo = models.EmailField(max_length=40)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField()
    is_active = models.BooleanField(default=True)

class Pasajero(models.Model):
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    cedula = models.IntegerField()
    correo = models.EmailField(max_length=40)
    tc = models.IntegerField()
    cvv = models.BooleanField()
    fecha_vencimiento = models.DateTimeField()
    fecha_inscripcion = models.DateTimeField()
    is_active = models.BooleanField(default=True)

class Arrendamiento(models.Model):
    fecha = models.DateTimeField()
    zona = models.CharField(max_length=10, choices=[('norte', 'Norte'), ('sur', 'Sur'), ('oriente', 'Oriente'), ('occidente', 'Occidente')])
    valor = models.IntegerField()
    punto_inicial = models.CharField(max_length=100)
    punto_final = models.CharField(max_length=100)
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)
    pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE)
    fecha_arrendamiento = models.DateTimeField()
    estado = models.CharField(max_length=10, choices=[('pendiente', 'Pendiente'), ('asignado', 'Asignado'), ('en curso', 'En curso'), ('finalizado', 'Finalizado'), ('cancelado', 'Cancelado'), ('anulado', 'Anulado')])
