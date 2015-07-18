from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render

from .models import Klas, Rhetorica, Persoon

def index(request):
	recent_modifications = Persoon.objects.order_by('-wijziging')[:15]
	recent_klassen = Klas.objects.order_by('jaar')[:10]
	
	context = {
		'recent_modifications': recent_modifications,
		'recent_klassen': recent_klassen
	}
	return render(request, 'alumni/index.html', context)
	
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

def persoondetail(request, persoon_id):
	try:
		persoon = Persoon.objects.get(pk=persoon_id)
	except Persoon.DoesNotExist:
		raise Http404("Persoon niet gevonden.")
	return render(request, 'alumni/detail.html', {'persoon': persoon})