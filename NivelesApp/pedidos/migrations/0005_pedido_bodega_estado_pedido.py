# Generated by Django 4.2.7 on 2023-11-14 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0004_alter_pedido_bodega_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido_bodega',
            name='estado_Pedido',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Confirmado', 'Confirmado'), ('Denegado', 'Denegado')], default='Pendiente', verbose_name='Estado'),
        ),
    ]
