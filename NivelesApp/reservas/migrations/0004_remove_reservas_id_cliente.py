# Generated by Django 4.2.7 on 2023-11-11 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0003_alter_reservas_estado_reserva_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservas',
            name='id_Cliente',
        ),
    ]
