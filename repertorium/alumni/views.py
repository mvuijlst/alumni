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
def az(request, letter):
	
	if letter:
		letter = letter[0].upper()
	else:
		letter = "A"
	
	try:
		personen = Persoon.objects.filter(achternaam__startswith=letter
			).exclude(rhetorica__exact=None
			).extra(select={'anaam': 'lower(achternaam)'}
			).order_by('anaam', 'voornaam')
	except Persoon.DoesNotExist:
		raise Http404("Geen alumni gevonden.")
	
	context = {
		'personen': personen,
		'letter': letter
	}
	
	return render(request, 'alumni/az.html', context)

@login_required
def rapport(request):
	return render(request, 'alumni/rapport.html')
	
@login_required
def moetbetalen(request):
	
	if datetime.now().month<7:
		schooljaar = datetime.now().year-1
	else:
		schooljaar = datetime.now().year

	personen = Persoon.objects.raw("""
		SELECT p.id, p.voornaam, p.achternaam, r.jaar, r.richting, a.adres, c.contactdata email
		FROM alumni_persoon p 
			inner join alumni_rhetorica r on p.rhetorica_id=r.id
			left outer join alumni_adres a on p.id=a.persoon_id
			left outer join alumni_contact c on p.id=c.persoon_id
		WHERE
			r.jaar < {0} and  
			p.overleden=0 and
			p.contacteren=1 and
			(a.geldig=1 or a.id is null) and 
			(c.contacttype='email' or c.id is null) and
			p.id not in (select persoon_id from alumni_betaling 
		                 where betalingsjaar={0} or soortbetaling_id<>2)
		GROUP BY p.id
		ORDER BY r.jaar, r.richting, p.achternaam""".format(schooljaar))

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
		
	personen = Persoon.objects.raw("""
		SELECT p.id, p.voornaam, p.achternaam, r.jaar, r.richting, a.adres, c.contactdata email
		FROM alumni_persoon p 
			inner join alumni_rhetorica r on p.rhetorica_id=r.id
			inner join alumni_betaling b on p.id=b.persoon_id
			left outer join alumni_adres a on p.id=a.persoon_id
			left outer join alumni_contact c on p.id=c.persoon_id
		WHERE
			r.jaar < {0} and 
			b.betalingsjaar in ({1},{2},{3}) and
			p.overleden=0 and
			p.contacteren=1 and
			(a.geldig=1 or a.id is null) and 
			(c.contacttype='email' or c.id is null) and 
			p.id not in (select persoon_id from alumni_betaling 
						 where betalingsjaar=2015 or soortbetaling_id=2)
		GROUP BY p.id
		ORDER BY r.jaar, r.richting, p.achternaam""".format(schooljaar,schooljaar-1,schooljaar-2,schooljaar-3))
	
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
	
	personen = Persoon.objects.raw("""
		SELECT p.id, p.voornaam, p.achternaam, r.jaar, r.richting, a.adres, c.contactdata email
		FROM alumni_persoon p 
			inner join alumni_rhetorica r on p.rhetorica_id=r.id
			left outer join alumni_betaling b on p.id=b.persoon_id
			left outer join alumni_adres a on p.id=a.persoon_id
			left outer join alumni_contact c on p.id=c.persoon_id
		WHERE
			(r.jaar = {0} or b.betalingsjaar={0} or b.soortbetaling_id=2) and
			p.overleden=0 and
			p.contacteren=1 and
			(a.geldig=1 or a.id is null) and 
			(c.contacttype='email' or c.id is null)
		GROUP BY p.id
		ORDER BY r.jaar, r.richting, p.achternaam
		""".format(schooljaar))
	
	context = {
		'personen': personen,
		'titel': 'Moet AB krijgen',
		'uitleg': """ <p>Lijst van mensen die </p>
			<ol><li>lid zijn, of vorig schooljaar afgestudeerd</li>
				<li>niet overleden zijn</li>
				<li>niet gezegd hebben dat ze niet meer willen gecontacteerd worden</li>
				<li>en die een geldig adres hebben</li>
			</ol>"""
	}
	
	return render(request, 'alumni/adreslijst.html', context)