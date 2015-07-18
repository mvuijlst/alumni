from django.http import HttpResponse

from .models import Klas, Persoon

def index(request):
	recent_modifications = Persoon.objects.order_by('wijziging')[:10]
	output= ', '.join([str(p) for p in recent_modifications])
	return HttpResponse(output)
	
def klaslijst(request, klas_id):
	return HttpResponse("Klaslijst voor %s." % klas_id)

def persoondetail(request, persoon_id):
	return HttpResponse("Detail voor persoon %s." % persoon_id)