# Generated by Django 3.0.4 on 2020-07-06 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=200, verbose_name='Descripcion'),
        ),
    ]
