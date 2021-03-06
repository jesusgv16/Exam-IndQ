# Generated by Django 3.0.4 on 2020-07-06 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Titulo')),
                ('description', models.CharField(max_length=200, verbose_name='Descripcion')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('imagen', models.ImageField(upload_to='images')),
                ('attendances', models.IntegerField(verbose_name='Asistencias')),
                ('WillYouAttend', models.CharField(choices=[('1', 'True'), ('0', 'False')], max_length=1)),
                ('longitud', models.CharField(max_length=120, verbose_name='longitud')),
                ('latitud', models.CharField(max_length=120, verbose_name='latitud')),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
            },
        ),
    ]
