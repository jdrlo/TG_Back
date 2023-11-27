# Generated by Django 4.2.4 on 2023-09-26 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id_Articulos', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_Producto', models.CharField(max_length=30, verbose_name='Nombre Producto')),
                ('precio_Producto', models.IntegerField(verbose_name='Precio Producto')),
                ('costo_Producto', models.IntegerField(verbose_name='Costo Producto')),
                ('imagen_Producto', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Imagen Producto')),
            ],
        ),
    ]
