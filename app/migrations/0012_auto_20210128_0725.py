# Generated by Django 3.1.3 on 2021-01-28 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20210128_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicules',
            name='annee_vehicule',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='vehicules',
            name='compteur_vehicule',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='vehicules',
            name='quantite_vehicule',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='vehicules',
            name='vendu',
            field=models.IntegerField(default=0),
        ),
    ]