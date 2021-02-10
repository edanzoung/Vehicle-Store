from django.db import models
from django.core.validators import RegexValidator
from app.storage import OverwriteStorage
from datetime import datetime
custom_store = OverwriteStorage()
date_now="{0}/{1}/{2}".format(str(datetime.utcnow().day),
                              str(datetime.utcnow().month),
                              str(datetime.utcnow().year))
# Create your models here.
class Vehicules(models.Model):
    MARQUES = (
        ('ACURA', 'ACURA'),
        ('ALPHA-ROMEO', 'ALPHA-ROMEO'),
        ('ALVIS', 'ALVIS'),
        ('ASTON-MARTIN', 'ASTON-MARTIN'),
        ('AUDI', 'AUDI'),
        ('BENTLEY', 'BENTLEY'),
        ('BMW', 'BMW'),
        ('BUGATTI', 'BUGATTI'),
        ('BUICK', 'BUICK'),
        ('CADILLAC', 'CADILLAC'),
        ('CITROËN', 'CITROËN'),
        ('CHEVROLET', 'CHEVROLET'),
        ('CHEVY', 'CHEVY'),
        ('CHRYSLER', 'CHRYSLER'),        
        ('DODGE', 'DODGE'),
        ('DS', 'DS'),
        ('EAGLE', 'EAGLE'),
        ('FERRARI', 'FERRARI'),
        ('FIAT', 'FIAT'),
        ('FORD', 'FORD'),
        ('GMC', 'GMC'),
        ('HONDA', 'HONDA'),
        ('HUMMER', 'HUMMER'),
        ('HYUNDAI', 'HYUNDAI'),
        ('INFINITI', 'INFINITI'),
        ('ISUZU', 'ISUZU'),
        ('JAGUAR', 'JAGUAR'),
        ('JEEP', 'JEEP'),
        ('KIA', 'KIA'),
        ('KTM', 'KTM'),
        ('LAMBORGHINI', 'LAMBORGHINI'),
        ('LAND-ROVER', 'LAND-ROVER'),
        ('LEXUS', 'LEXUS'),
        ('LOTUS', 'LOTUS'),
        ('MASERATI', 'MASERATI'),
        ('MAZDA', 'MAZDA'),
        ('MCLAREN', 'MCLAREN'),
        ('MERCEDES-BENZ', 'MERCEDES-BENZ'),
        ('MINI', 'MINI'),
        ('MITSUBISHI', 'MITSUBISHI'),
        ('NISSAN', 'NISSAN'),
        ('OPEL', 'OPEL'),
        ('PAGANI', 'PAGANI'),
        ('PEUGEOT', 'PEUGEOT'),
        ('PORSCHE', 'PORSCHE'),
        ('ROLLS-ROYCE', 'ROLLS-ROYCE'),
        ('SUBARU', 'SUBARU'),
        ('SUZUKI', 'SUZUKI'),
        ('TESLA', 'TESLA'),
        ('TOYOTA', 'TOYOTA'),
        ('VOLKSWAGEN', 'VOLKSWAGEN'),
        ('VOLVO', 'VOLVO'),
        ('WEBER', 'WEBER'),
        ('WIESMANN', 'WIESMANN'),
        ('ZASTAVA', 'ZASTAVA'),
        ('ZENVO', 'ZENVO'))

    ETAT = (
        ('N/A', 'N/A'),
        ('NEUF', 'NEUF'),
        ('SECONDE-MAIN', 'SECONDE-MAIN'))

    BOITE = (
        ('N/A', 'N/A'),
        ('AUTOMATIQUE', 'AUTOMATIQUE'),
        ('MANUELLE', 'MANUELLE'),
        ('MIXTE', 'MIXTE'))

    CARBURANT = (
        ('N/A', 'N/A'),
        ('ELECTRIQUE', 'ELECTRIQUE'),
        ('ESSENCE', 'ESSENCE'),
        ('DIESEL', 'DIESEL'),
        ('HYBRIDE', 'HYBRIDE'))

    VENDU = (
        ('OUI', 'OUI'),
        ('NON', 'NON'))
    
    image1_vehicule = models.ImageField(storage=custom_store,upload_to='static/images/',default=' ')
    image2_vehicule = models.ImageField(storage=custom_store,upload_to='static/images/',default=' ')
    image3_vehicule = models.ImageField(storage=custom_store,upload_to='static/images/',default=' ')
    image4_vehicule = models.ImageField(storage=custom_store,upload_to='static/images/',default=' ')
    image5_vehicule = models.ImageField(storage=custom_store,upload_to='static/images/',default=' ')
    image6_vehicule = models.ImageField(storage=custom_store,upload_to='static/images/',default=' ')
    image7_vehicule = models.ImageField(storage=custom_store,upload_to='static/images/',default=' ')
    image8_vehicule = models.ImageField(storage=custom_store,upload_to='static/images/',default=' ')
    image9_vehicule = models.ImageField(storage=custom_store,upload_to='static/images/',default=' ')
    image10_vehicule = models.ImageField(storage=custom_store,upload_to='static/images/',default=' ')
    marque_vehicule = models.CharField(max_length=100,choices=MARQUES,blank=True)
    modele_vehicule = models.CharField(max_length=100,blank=True)
    annee_vehicule = models.IntegerField(default=0)
    couleur_vehicule = models.CharField(max_length=100,blank=True)
    etat_vehicule = models.CharField(max_length=100,choices=ETAT,blank=True)
    compteur_vehicule = models.IntegerField(default=0)
    transmission_vehicule = models.CharField(max_length=100,choices=BOITE,blank=True)
    carburant_vehicule = models.CharField(max_length=100,choices=CARBURANT,blank=True)
    description_vehicule = models.TextField(max_length=200,blank=True)
    quantite_vehicule = models.IntegerField(default=0)
    prix_vehicule = models.CharField(max_length=100,blank=True)
    vendu = models.CharField(max_length=10,choices=VENDU,blank=True)
    date = models.CharField(max_length=100,default=date_now,blank=True)
    

