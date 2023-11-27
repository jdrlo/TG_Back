# Generated by Django 4.2.6 on 2023-10-12 22:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('musica', '0002_alter_musica_cancion'),
    ]

    operations = [
        migrations.AddField(
            model_name='musica',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='musica',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]