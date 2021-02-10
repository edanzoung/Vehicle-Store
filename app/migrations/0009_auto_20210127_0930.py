# Generated by Django 3.1.3 on 2021-01-27 09:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210127_0333'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicules',
            name='carburant_vehicule',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicules',
            name='transmission_vehicule',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vehicules',
            name='couleur_vehicule',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicules',
            name='etat_vehicule',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicules',
            name='image_vehicule',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicules',
            name='marque_vehicule',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicules',
            name='modele_vehicule',
            field=models.CharField(max_length=100),
        ),
    ]
