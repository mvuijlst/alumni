from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from datetime import datetime, timedelta

from .models import Klas, Rhetorica, Persoon, Contact, Beroep, Adres, Betaling, Gebeurtenis, Klasfoto, Persoonfoto

@login_required
def index(request):
	wijzigingen = Persoon.objects.order_by('-wijziging')[:15]
	personalia = Gebeurtenis.objects.filter(
		datum__gt=datetime.today()-timedelta(weeks=26)
		).order_by('gebeurtenistype','persoon__rhetorica__jaar')
	overleden = Persoon.objects.filter(
		sterfdatum__gt=datetime.today()-timedelta(weeks=26)
		).order_by('rhetorica__jaar')
	adreswijzigingen = Adres.objects.filter(
		geldig__exact=True
		).filter(persoon__overleden__exact=False
		).filter(persoon__publiek__exact=True
		).filter(van__gt=datetime.today()-timedelta(weeks=26)
		).order_by('persoon__rhetorica__jaar')
	
	context = {
		'wijzigingen': wijzigingen,
		'personalia': personalia,
		'overleden': overleden,
		'adreswijzigingen': adreswijzigingen
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
	persoonfotos = Persoonfoto.objects.filter(persoon=persoon_id).order_by('-datum')
	
	context = {
		'persoon': persoon,
		'contacten': contacten,
		'beroepen': beroepen,
		'adressen': adressen,
		'gebeurtenissen' : gebeurtenissen,
		'betalingen': betalingen,
		'persoonfotos': persoonfotos 
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
			).extra(select={'anaam': """replace(replace(lower(achternaam),'ù','u'),'ú','u')"""}
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
			a.geldig=1 and 
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
			<li>en die een geldig postadres hebben</li>
		</ol>"""
	}
	
	return render(request, 'alumni/adreslijst.html', context)

@login_required
def vroegerbetaald(request,alle):
	
	if datetime.now().month<7:
		schooljaar = datetime.now().year-1
	else:
		schooljaar = datetime.now().year
	
	if int(alle) > 0:
		zoekscope = 'is not null'
		titel = 'Alle ex-leden'
		wanneer = 'ooit lidgeld betaald hebben'
	else:	
		zoekscope = 'in (' + str(schooljaar-1) + ',' + str(schooljaar-2) + ',' + str(schooljaar-3) + ')'
		titel = 'Recente ex-leden'
		wanneer = 'lidgeld betaald hebben vorig jaar, of het jaar daarvoor, of het jaar daarvoor'
		
	personen = Persoon.objects.raw("""
		SELECT p.id, p.voornaam, p.achternaam, r.jaar, r.richting, a.adres, c.contactdata email
		FROM alumni_persoon p 
			inner join alumni_rhetorica r on p.rhetorica_id=r.id
			inner join alumni_betaling b on p.id=b.persoon_id
			left outer join alumni_adres a on p.id=a.persoon_id
			left outer join alumni_contact c on p.id=c.persoon_id
		WHERE
			r.jaar < {0} and 
			b.betalingsjaar {1} and
			p.overleden=0 and
			p.contacteren=1 and
			a.geldig=1 and 
			(c.contacttype='email' or c.id is null) and 
			p.id not in (select persoon_id from alumni_betaling 
						 where betalingsjaar={0} or soortbetaling_id=2)
		GROUP BY p.id
		ORDER BY r.jaar, r.richting, p.achternaam""".format(schooljaar,zoekscope))
	
	context = {
		'titel': titel,
		'personen': personen,
		'uitleg': """<p>Lijst van mensen die </p>
			<ol><li>zouden moeten betalen (afgestudeerd meer dan een jaar geleden)</li>
			<li>nog niet betaald hebben voor dit jaar</li>
			<li>niet overleden zijn</li>
			<li>niet gezegd hebben dat ze niet meer willen gecontacteerd worden</li>
			<li>{0}</li>
			<li>en die een geldig postadres hebben</li>
		</ol>""".format(wanneer)
	}
	
	return render(request, 'alumni/adreslijst.html', context)
	
@login_required
def moetABkrijgen(request):
	
	if datetime.now().month<7:
		schooljaar = datetime.now().year-1
	else:
		schooljaar = datetime.now().year
	
	personen = Persoon.objects.raw("""
		SELECT p.id, p.voornaam, p.achternaam achternaam, r.jaar jaar, r.richting richting, a.adres, c.contactdata email
		FROM alumni_persoon p 
			inner join alumni_rhetorica r on p.rhetorica_id=r.id
			left outer join alumni_betaling b on p.id=b.persoon_id
			left outer join alumni_adres a on p.id=a.persoon_id
			left outer join alumni_contact c on p.id=c.persoon_id
		WHERE
			(r.jaar = {0} or b.betalingsjaar={0} or b.soortbetaling_id=2) and
			p.overleden=0 and
			p.contacteren=1 and
			a.geldig=1 and 
			(c.contacttype='email' or c.id is null)
		GROUP BY p.id
		
		UNION
		
		SELECT p.id, p.voornaam, p.achternaam, null jaar, s.omschrijving richting, a.adres, c.contactdata email
		FROM alumni_persoon p 
			inner join alumni_hoedanigheid h on h.persoon_id=p.id
			inner join alumni_soorthoedanigheid s on h.soorthoedanigheid_id = s.id
			left outer join alumni_adres a on p.id=a.persoon_id
			left outer join alumni_contact c on p.id=c.persoon_id
		WHERE
			p.overleden=0 and
			p.contacteren=1 and
			a.geldig=1 and 
			(c.contacttype='email' or c.id is null)
		GROUP BY p.id
			
		ORDER BY achternaam, jaar, richting 
		
		""".format(schooljaar))
	
	context = {
		'personen': personen,
		'titel': 'Adressenlijst Allegro Barbara',
		'uitleg': """ <p>Lijst van mensen die </p>
			<ol><li>AB moeten krijgen, omdat ze <ul><li>dit jaar betalend lid zijn, of </li><li>vorig schooljaar afgestudeerd zijn, of</li><li>oud-leraar, raad van bestuur e.d. zijn</li></ul></li>
				<li>niet overleden zijn</li>
				<li>niet gezegd hebben dat ze niet meer willen gecontacteerd worden</li>
				<li>en die een geldig postadres hebben</li>
			</ol>"""
	}
	
	return render(request, 'alumni/adreslijst.html', context)

@login_required
def geenadres(request):
	personen = Persoon.objects.raw("""
		SELECT p.id, p.voornaam, p.achternaam, r.jaar, r.richting, c.contactdata email,  
			if(length(a.adres)>0, 
				concat(coalesce(a.adres,''), '\n[', coalesce(a.van,''),' - ',coalesce(a.tot,''), ']'), 
				null) adres
		FROM alumni_persoon p 
			inner join alumni_rhetorica r on p.rhetorica_id=r.id
			left outer join alumni_contact c on p.id=c.persoon_id
			left outer join 
				(select a1.adres, a1.persoon_id, a1.geldig, a1.van, a1.tot
                 from alumni_adres a1
					inner join (
    					select persoon_id, max(van) as recentsteongeldig
    					from alumni_adres
    					where geldig=0
    					group by persoon_id
   					) a2 on a1.persoon_id=a2.persoon_id and 
                 			a1.van = recentsteongeldig
                ) a on p.id=a.persoon_id
		WHERE
			p.overleden=0 and
			p.contacteren=1  and
			(a.geldig=0 or a.geldig is null) and 
			(c.contacttype='email' or c.id is null) and
			p.id not in (
				select persoon_id
				from alumni_adres
				group by persoon_id
				having sum(geldig)>0
			)
		GROUP BY p.id
		ORDER BY  r.jaar, r.richting, p.achternaam""")
	
	context = {
		'titel': 'Alumni zonder (geldig) adres',
		'personen': personen,
		'uitleg': """<p>Lijst van mensen die </p>
			<ol><li>niet overleden zijn</li>
			<li>niet gezegd hebben dat ze niet meer willen gecontacteerd worden</li>
			<li>en die geen (geldig) postadres hebben</li>
		</ol>
		<p>Tussen [vierkante haakjes] de datum van/tot van het laatst gekende ongeldige adres."""
	}
	
	return render(request, 'alumni/adreslijst.html', context)
	
@login_required
def nietalumni(request):
	
	try:
		personen = Persoon.objects.filter(rhetorica__exact=None
			).order_by('achternaam', 'voornaam')
	except Persoon.DoesNotExist:
		raise Http404("Geen niet-alumni gevonden.")
	
	context = {
		'personen': personen
	}
	
	return render(request, 'alumni/nietalumni.html', context)