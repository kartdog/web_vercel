# Generated by Django 5.0.6 on 2024-05-26 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_empleado_tipo_mecanico'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='descripcion',
            field=models.TextField(default='sin desc', max_length=550),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='servicio',
            name='descripcion_servicio',
            field=models.TextField(max_length=550),
        ),
    ]
