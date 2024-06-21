# Generated by Django 5.0.6 on 2024-05-26 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_servicio_costo_servicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='tipo_mecanico',
            field=models.CharField(choices=[('NOM', 'NoMecanico'), ('GEN', 'General'), ('ELE', 'Electrico'), ('MOT', 'Motriz'), ('FRE', 'Frenos')], default='NOM', max_length=20),
        ),
    ]