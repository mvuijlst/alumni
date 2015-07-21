from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from datetime import datetime

from .models import Klas, Rhetorica, Persoon, Contact, Beroep, Adres, Betaling, Gebeurtenis

@login_required
def index(request):
	recent_modifications = Persoon.objects.order_by('-wijziging')[:15]
	recent_klassen = Klas.objects.order_by('-jaar')
	
	context = {
		'recent_modifications': recent_modifications,
		'recent_klassen': recent_klassen
	}
	return render(request, 'alumni/index.html', context)

def info(request):
	return render(request, 'alumni/info.html')
		
@login_required
def klaslijst(request, klas_id):
	try:
		klas = Klas.objects.get(pk=klas_id)
	except Klas.DoesNotExist:
		raise Http404("Klas niet gevonden.")
	personen = Persoon.objects.filter(rhetorica__klas=klas_id).order_by('rhetorica__richting', 'achternaam', 'voornaam')
	aantal_klassen = Rhetorica.objects.filter(klas=klas_id).count()
	context = {
		'klas': klas,
		'personen': personen,
		'aantal_klassen': aantal_klassen
	}
	return render(request, 'alumni/klaslijst.html', context)

@login_required
def persoondetail(request, persoon_id):
	try:
		persoon = Persoon.objects.get(pk=persoon_id)
	except Persoon.DoesNotExist:
		raise Http404("Persoon niet gevonden.")
	
	contacten = Contact.objects.filter(persoon=persoon_id).filter(geldig=True).order_by('contacttype', '-van', '-tot')
	beroepen = Beroep.objects.filter(persoon=persoon_id).order_by('-featured', '-van', '-tot')
	adressen = Adres.objects.filter(persoon=persoon_id).order_by('-van', '-tot')
	betalingen = Betaling.objects.filter(persoon=persoon_id).order_by('-betalingsjaar', '-datum')
	gebeurtenissen = Gebeurtenis.objects.filter(persoon=persoon_id).order_by('-datum')
	
	context = {
		'persoon': persoon,
		'contacten': contacten,
		'beroepen': beroepen,
		'adressen': adressen,
		'gebeurtenissen' : gebeurtenissen,
		'betalingen': betalingen,
		'aantal_contacten': len(contacten),
		'aantal_beroepen': len(beroepen),
		'aantal_adressen': len(adressen),
		'aantal_gebeurtenissen' : len(gebeurtenissen),
		'aantal_betalingen': len(betalingen)		
	}
	return render(request, 'alumni/detail.html', context)

@login_required
def moetbetalen(request):
	ditjaarbetaald = Betaling.objects.exclude(
		betalingsjaar=datetime.now().year
	).exclude(
		soortbetaling=2
	).order_by(
		'persoon_id'
	).values_list(
		'persoon_id', flat=True
	).distinct()
	
	personen = Persoon.objects.filter(
		overleden=0
	).filter(
		rhetorica__jaar__lt=datetime.now().year
	).exclude(
		id__in=ditjaarbetaald
	).filter(
		contacteren=1
	).order_by(
		'rhetorica__jaar', 'achternaam', 'voornaam'
	)

	#personen = Persoon.objects.filter(overleden=0).filter(id__in=vroegerbetaald)

	context = {
		'personen': personen
	}
	
	return render(request, 'alumni/moetbetalen.html', context)

@login_required
def vroegerbetaald(request):
	vroegerbetaald = Betaling.objects.exclude(
		betalingsjaar=datetime.now().year
	).exclude(
		soortbetaling=2
	).filter(
		Q(betalingsjaar=datetime.now().year-1)|Q(betalingsjaar=datetime.now().year-2)|Q(betalingsjaar=datetime.now().year-3)
	).order_by(
		'persoon_id'
	).values(
		'persoon_id'
	).distinct()
	
	personen = Persoon.objects.filter(
		overleden=0
	).filter(
		rhetorica__jaar__lt=datetime.now().year
	).filter(
		id__in=vroegerbetaald
	).filter(
		contacteren=1
	).order_by(
		'rhetorica__jaar', 'achternaam', 'voornaam'
	)
	
	context = {
		'personen': personen
	}
	
	return render(request, 'alumni/vroegerbetaald.html', context)