from django.shortcuts import redirect, render
from django.views import View
from app import models
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from app.forms import ContactForm , Commande
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def home(request):
    title="ACCUEIL"
    return render(request, "index.html",
                  {'cars' : models.Vehicule.objects.all(),'title' : title})

def menu(request):
    marques = models.Vehicule.objects.all()
    return render(request, "base.html",{'marques': marques,'len_marque': range(len(marques))})

def vehicule_detail(request,id):
    title="DETAILS"
    
    return render(request, "details-vehicule.html",
                  {'cars' : models.Vehicule.objects.get(id=id),'title' : title})

def vehicules(request):
    title="NOS VEHICULES"
    
    vehicle_list = models.Vehicule.objects.all()

    query = request.GET.get('q')
    
    if query is not None:
        vehicle_list = models.Vehicule.objects.filter(
            Q(marque_vehicule__icontains=query) | Q(modele_vehicule__icontains=query) |
            Q(annee_vehicule__icontains=query) | Q(couleur_vehicule__icontains=query) |
            Q(etat_vehicule__icontains=query) | Q(carburant_vehicule__icontains=query) |
            Q(compteur_vehicule__icontains=query) | Q(transmission_vehicule__icontains=query)).distinct()
    elif query is None:
        vehicle_list = models.Vehicule.objects.all()
        

    paginator = Paginator(vehicle_list, 6) # Show 6 vehicles per page.    
    page_number = request.GET.get('page')
    
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    precedent_num=int(page_obj.number)-1
    suivant_num=int(page_obj.number)+1

    context = {'cars' : models.Vehicule.objects.all(),'list_vehicle_size':int(len(vehicle_list)),
                   'page_obj': page_obj,'title' : title,'precedent_num':precedent_num,'suivant_num':suivant_num}
    return render(request, "vehicules.html", context)

def nos_services(request):
    title="NOS SERVICES"
    return render(request, "nos-services.html",
                  {'title' : title})

def a_propos(request):
    title="A PROPOS"
    return render(request, "about.html",
                  {'title' : title})

def nous_contacter(request):
    title="NOUS CONTACTER"

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "CONTACT G-A-R-T"
            body = {
                'prenom': form.cleaned_data['prenom'],
                'nom_de_famille': form.cleaned_data['nom_de_famille'],
                'email': form.cleaned_data['email'],
                'numero': form.cleaned_data['numero'],
                'pays': form.cleaned_data['pays'],
                'message':form.cleaned_data['message']}

            message = "\n".join(body.values())

            try:
                #send_mail( subject,message,'elkanazoungrana@gmail.com',['elkanazoungrana@gmail.com'])
                return redirect ("success")
            except Exception as e:
                return HttpResponse(e)           
      
    form = ContactForm()
    return render(request, "contact.html",{'title' : title,'form':form})

def commander(request,id):
    title="COMMANDES"
    cars= models.Vehicule.objects.get(id=id)
    
    if request.method == 'POST':
        form = Commande(request.POST)
        if form.is_valid():
            form.cleaned_data['vehicule']=str(cars.marque_vehicule)
            subject = "COMMANDE G-A-R-T"
            body = {
                    'prenom': form.cleaned_data['prenom'], 
                    'nom_de_famille': form.cleaned_data['nom_de_famille'], 
                    'email': form.cleaned_data['email'],
                    'numero': form.cleaned_data['numero'],
                    'pays': form.cleaned_data['pays'],
                    'vehicule':form.cleaned_data['vehicule']}

            message = "\n".join(body.values())
            try:
                #send_mail( subject,message,'elkanazoungrana@gmail.com',['elkanazoungrana@gmail.com'])
                return redirect ("success-commande")
            except Exception as e:
                return HttpResponse(e)
      
    form = Commande()
    return render(request, "commande.html",{'cars' :cars,'title' : title,'form':form})

def success_page(request):
    return render(request, "success.html")

def success_commande_page(request):
    return render(request, "success-commande.html")

def handler404(request,exception):
    return render(request, '404.html', status=404)
def handler500(request):
    return render(request, '500.html', status=500)
