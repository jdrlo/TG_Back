# Generated by Django 4.2.4 on 2023-10-03 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id_Foto', models.AutoField(primary_key=True, serialize=False)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='publicidad/%Y%m', verbose_name='Foto')),
                ('precio_Palco', models.IntegerField(blank=True, null=True, verbose_name='Precio Palco')),
                ('cantidad_Personas', models.IntegerField(default=0, verbose_name='Cantidad Personas')),
            ],
        ),
    ]
