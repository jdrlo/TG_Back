# Generated by Django 4.2.7 on 2023-11-09 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido_bodega',
            name='id_Usuario',
        ),
        migrations.RemoveField(
            model_name='pedido_mesero',
            name='id_Usuario',
        ),
    ]
