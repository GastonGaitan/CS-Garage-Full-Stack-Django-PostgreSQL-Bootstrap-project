# Generated by Django 4.1.7 on 2023-02-27 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosVenta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('dni', models.CharField(max_length=8, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=80)),
                ('localidad', models.CharField(max_length=100)),
                ('tipo_cliente', models.CharField(max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='auto',
            name='image',
            field=models.ImageField(default=None, upload_to='serviciosVenta/photos'),
        ),
        migrations.AddField(
            model_name='auto',
            name='dni_anterior_duenio',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='serviciosVenta.cliente'),
        ),
    ]
