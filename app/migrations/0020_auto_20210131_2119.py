# Generated by Django 3.1 on 2021-01-31 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20210131_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicules',
            name='carburant_vehicule',
            field=models.CharField(blank=True, choices=[('ELECTRIQUE', 'ELECTRIQUE'), ('ESSENCE', 'ESSENCE'), ('DIEZEL', 'DIEZEL'), ('HYBRIDE', 'HYBRIDE')], max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicules',
            name='couleur_vehicule',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicules',
            name='date',
            field=models.CharField(blank=True, default='31/1/2021', max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicules',
            name='description_vehicule',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='vehicules',
            name='etat_vehicule',
            field=models.CharField(blank=True, choices=[('NEUF', 'NEUF'), ('SECONDE-MAIN', 'SECONDE-MAIN')], max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicules',
            name='marque_vehicule',
            field=models.CharField(blank=True, choices=[('ACURA', 'ACURA'), ('ALVIS', 'ALVIS'), ('AUDI', 'AUDI'), ('BENTLEY', 'BENTLEY'), ('BMW', 'BMW'), ('BUGATTI', 'BUGATTI'), ('BUICK', 'BUICK'), ('CADILLAC', 'CADILLAC'), ('CHEVY', 'CHEVY'), ('CHRYSLER', 'CHRYSLER'), ('CITROËN', 'CITROËN'), ('DODGE', 'DODGE'), ('DS', 'DS'), ('EAGLE', 'EAGLE'), ('FERRARI', 'FERRARI'), ('FIAT', 'FIAT'), ('FORD', 'FORD'), ('GMC', 'GMC'), ('HONDA', 'HONDA'), ('HUMMER', 'HUMMER'), ('HYUNDAI', 'HYUNDAI'), ('INFINITI', 'INFINITI'), ('ISUZU', 'ISUZU'), ('JAGUAR', 'JAGUAR'), ('JEEP', 'JEEP'), ('KIA', 'KIA'), ('KTM', 'KTM'), ('LAMBORGHINI', 'LAMBORGHINI'), ('LAND-ROVER', 'LAND-ROVER'), ('LEXUS', 'LEXUS'), ('LOTUS', 'LOTUS'), ('MASERATI', 'MASERATI'), ('MAZDA', 'MAZDA'), ('MERCEDES-BENZ', 'MERCEDES-BENZ'), ('MINI', 'MINI'), ('MITSUBISHI', 'MITSUBISHI'), ('NISSAN', 'NISSAN'), ('OPEL', 'OPEL'), ('PAGANI', 'PAGANI'), ('PEUGEOT', 'PEUGEOT'), ('PORSCHE', 'PORSCHE'), ('ROLLS-ROYCE', 'ROLLS-ROYCE'), ('SUBARU', 'SUBARU'), ('SUZUKI', 'SUZUKI'), ('TESLA', 'TESLA'), ('TOYOTA', 'TOYOTA'), ('VOLKSWAGEN', 'VOLKSWAGEN'), ('VOLVO', 'VOLVO'), ('WEBER', 'WEBER'), ('WIESMANN', 'WIESMANN'), ('ZASTAVA', 'ZASTAVA'), ('ZENVO', 'ZENVO')], max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicules',
            name='modele_vehicule',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicules',
            name='prix_vehicule',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicules',
            name='transmission_vehicule',
            field=models.CharField(blank=True, choices=[('AUTOMATIQUE', 'AUTOMATIQUE'), ('MANUELLE', 'MANUELLE'), ('MIXTE', 'MIXTE')], max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicules',
            name='vendu',
            field=models.CharField(blank=True, choices=[('OUI', 'OUI'), ('NON', 'NON')], max_length=10),
        ),
    ]