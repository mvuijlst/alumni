from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from datetime import datetime

from .models import Klas, Rhetorica, Persoon, Contact, Beroep, Adres, Betaling, Gebeurtenis, Klasfoto

@login_required
def index(request):
	recent_modifications = Persoon.objects.order_by('-wijziging')[:15]
	
	context = {
		'recent_modifications': recent_modifications,
	}
	return render(request, 'alumni/index.html', context)

def info(request):
	return render(request, 'alumni/info.html')

@login_required
def decennium(request,decennium):
	dec=int(decennium[:3])
	try:
		klassen=Klas.objects.filter(jaar__startswith=dec).order_by('jaar', 'klasnaam')
	except Klas.DoesNotExist:
		raise Http404("Geen klassen gevonden.")
	context = { 
		'klassen': klassen,
		'decennium': decennium
	}
	return render(request, 'alumni/decennium.html',context)

@login_required
def klaslijst(request, klas_id):
	try:
		klas = Klas.objects.get(pk=klas_id)
	except Klas.DoesNotExist:
		raise Http404("Klas niet gevonden.")
	personen = Persoon.objects.filter(rhetorica__klas=klas_id).order_by('rhetorica__richting', 'achternaam', 'voornaam')
	adressen = Adres.objects.filter(persoon__rhetorica__klas_id=klas_id).filter(persoon__overleden=0).filter(geldig=1)
	klasfotos = Klasfoto.objects.filter(klas=klas_id).order_by('datum')
	aantal_klassen = Rhetorica.objects.filter(klas=klas_id).count()
	context = {
		'klas': klas,
		'personen': personen,
		'adressen' : adressen,
		'klasfotos': klasfotos,
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
		'betalingen': betalingen	
	}
	return render(request, 'alumni/detail.html', context)

@login_required
def rapport(request):
	return render(request, 'alumni/rapport.html')
	
@login_required
def moetbetalen(request):
	
	if datetime.now().month<7:
		schooljaar = datetime.now().year-1
	else:
		schooljaar = datetime.now().year
		
	ditjaarbetaald = Betaling.objects.exclude(
		betalingsjaar=schooljaar
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
		rhetorica__jaar__lt=schooljaar
	).exclude(
		id__in=ditjaarbetaald
	).filter(
		contacteren=1
	).order_by(
		'-rhetorica__jaar', 'rhetorica__richting' ,'achternaam', 'voornaam'
	)

	#personen = Persoon.objects.filter(overleden=0).filter(id__in=vroegerbetaald)

	context = {
		'titel': 'Moeten betalen',
		'personen': personen,
		'uitleg': """<p>Lijst van mensen die </p>
			<ol><li>zouden moeten betalen (afgestudeerd meer dan een jaar geleden)</li>
			<li>nog niet betaald hebben voor dit jaar</li>
			<li>niet overleden zijn</li>
			<li>niet gezegd hebben dat ze niet meer willen gecontacteerd worden</li>
		</ol>"""
	}
	
	return render(request, 'alumni/adreslijst.html', context)

@login_required
def vroegerbetaald(request):
	
	if datetime.now().month<7:
		schooljaar = datetime.now().year-1
	else:
		schooljaar = datetime.now().year
		
	vroegerbetaald = Betaling.objects.filter(
		Q(betalingsjaar=schooljaar-1)|Q(betalingsjaar=schooljaar-2)|Q(betalingsjaar=schooljaar-3)
	).exclude(
		betalingsjaar=2015
	).exclude(
		soortbetaling=2
	).order_by(
		'persoon_id'
	).values(
		'persoon_id'
	).distinct()
	
	personen = Persoon.objects.filter(
		overleden=0
	).filter(
		rhetorica__jaar__lt=schooljaar
	).filter(
		id__in=vroegerbetaald
	).filter(
		contacteren=1
	).order_by(
		'-rhetorica__jaar', 'rhetorica__richting', 'achternaam', 'voornaam'
	)
	
	context = {
		'titel': 'Recente ex-leden',
		'personen': personen,
		'uitleg': """<p>Lijst van mensen die </p>
			<ol><li>zouden moeten betalen (afgestudeerd meer dan een jaar geleden)</li>
			<li>nog niet betaald hebben voor dit jaar</li>
			<li>niet overleden zijn</li>
			<li>niet gezegd hebben dat ze niet meer willen gecontacteerd worden</li>
			<li>lidgeld betaald hebben vorig jaar, of het jaar daarvoor, of het jaar daarvoor</li>
		</ol>"""
	}
	
	return render(request, 'alumni/adreslijst.html', context)
	
@login_required
def moetABkrijgen(request):
	
	if datetime.now().month<7:
		schooljaar = datetime.now().year-1
	else:
		schooljaar = datetime.now().year
	
	lid = Betaling.objects.filter(
		Q(betalingsjaar__exact=schooljaar)|Q(soortbetaling__exact=2)
	).order_by(
		'persoon_id'
	).values(
		'persoon_id'
	).distinct()
	
	personen = Persoon.objects.filter(
		overleden=0
	).filter(
		Q(rhetorica__klas__jaar__exact=schooljaar)|Q(id__in=lid)
	).filter(
		contacteren=1
	).order_by(
		'-rhetorica__jaar', 'rhetorica__richting', 'achternaam', 'voornaam'
	)
	
	adressen = Adres.objects.filter(
		Q(persoon__id__in=lid)|Q(persoon__rhetorica__jaar__exact=schooljaar)
	).filter(
		geldig=1
	)
	
	context = {
		'personen': personen,
		'adressen': adressen,
		'titel': 'Moet AB krijgen',
		'uitleg': """ <p>Lijst van mensen die </p>
			<ol><li>lid zijn, of vorig schooljaar afgestudeerd</li>
				<li>niet overleden zijn</li>
				<li>niet gezegd hebben dat ze niet meer willen gecontacteerd worden</li>
			</ol>"""
	}
	
	return render(request, 'alumni/adreslijst.html', context)