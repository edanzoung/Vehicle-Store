# Generated by Django 3.1.3 on 2021-01-27 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210127_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicules',
            name='prix_vehicule',
            field=models.CharField(max_length=100),
        ),
    ]
