from django.contrib import admin
from app.models import Vehicule

# Register your models here.

class Custom_Admin(admin.ModelAdmin):
    list_display=("marque_vehicule","modele_vehicule","annee_vehicule","transmission_vehicule")
    search_fields=("marque_vehicule","modele_vehicule","annee_vehicule","transmission_vehicule")
    filter_horizontal=()
    list_filter=()
    fieldsets=()

admin.site.register(Vehicule,Custom_Admin)

