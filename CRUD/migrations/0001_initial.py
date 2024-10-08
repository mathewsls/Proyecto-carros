# Generated by Django 5.1.1 on 2024-10-01 00:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('cedula', models.IntegerField()),
                ('correo', models.EmailField(max_length=40)),
                ('fecha_inscripcion', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pasajero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('cedula', models.IntegerField()),
                ('correo', models.EmailField(max_length=40)),
                ('tc', models.IntegerField()),
                ('cvv', models.BooleanField()),
                ('fecha_vencimiento', models.DateTimeField()),
                ('fecha_inscripcion', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=40)),
                ('modelo', models.CharField(max_length=40)),
                ('placa', models.CharField(max_length=10)),
                ('fecha_fabricacion', models.DateTimeField()),
                ('fecha_inicial_soat', models.DateTimeField()),
                ('fecha_final_soat', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Arrendamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('zona', models.CharField(choices=[('norte', 'Norte'), ('sur', 'Sur'), ('oriente', 'Oriente'), ('occidente', 'Occidente')], max_length=10)),
                ('valor', models.IntegerField()),
                ('punto_inicial', models.CharField(max_length=100)),
                ('punto_final', models.CharField(max_length=100)),
                ('fecha_arrendamiento', models.DateTimeField()),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('asignado', 'Asignado'), ('en curso', 'En curso'), ('finalizado', 'Finalizado'), ('cancelado', 'Cancelado'), ('anulado', 'Anulado')], max_length=10)),
                ('conductor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRUD.conductor')),
                ('pasajero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRUD.pasajero')),
            ],
        ),
        migrations.AddField(
            model_name='conductor',
            name='vehiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRUD.vehiculo'),
        ),
    ]
