# Generated by Django 4.2.7 on 2023-11-18 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_articulos_imagen_producto'),
        ('pedidos', '0008_remove_inventario_id_articulos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='cantidad_TotalVenta',
            field=models.IntegerField(default=0, verbose_name='Cantidad total vendido'),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='id_Articulos_Inventario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.articulos', verbose_name='Articulo'),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='pedidos_Bodega',
            field=models.IntegerField(default=0, verbose_name='pedido bodega'),
        ),
    ]
