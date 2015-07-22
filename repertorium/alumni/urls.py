from django.conf.urls import url
from . import views

urlpatterns = [
	# bv: /repertorium/
    url(r'^$', views.index, name='index'),
    # bv: /repertorium/decennium/1980
    url(r'^dec/(?P<decennium>[0-9]{4})$', views.decennium, name='decennium'),
    # bv: /repertorium/klas/123
    url(r'^klas/(?P<klas_id>[0-9]+)$', views.klaslijst, name='klaslijst'),
    # bv: /repertorium/p/6677
    url(r'^p/(?P<persoon_id>[0-9]+)$', views.persoondetail, name='detail'),
    # bv: /repertorium/info
    url(r'^info$', views.info, name='info'),
    # rapporten
    url(r'^moetbetalen$', views.moetbetalen, name='moetbetalen'),
    url(r'^vroegerbetaald$', views.vroegerbetaald, name='vroegerbetaald'),
]