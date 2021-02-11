"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from app import views
from django.contrib import admin
from django.conf.urls import handler404, handler500

urlpatterns = [
    path("", views.home, name="index"),
    path("details_vehicule/<id>/", views.vehicule_detail, name="details-vehicule"),
    path("vehicules/", views.vehicules, name="vehicules"),
    path("nos_services/", views.nos_services, name="nos-services"),
    path("a_propos/", views.a_propos, name="about"),
    path("commandes/<id>/", views.commander, name="commande"),
    path("nous_contacter/", views.nous_contacter, name="contact"),
    path("success/", views.success_page, name="success"),
    path("success_commande/", views.success_commande_page, name="success-commande"),
    path("admin/dashboard/", admin.site.urls)
]

handler404 = views.handler404
handler500 = views.handler500
