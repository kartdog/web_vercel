# Generated by Django 5.0.6 on 2024-05-25 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_servicio_pagina_servicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='empleados'),
        ),
    ]
