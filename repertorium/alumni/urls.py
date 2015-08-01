from django.conf import settings
from django.conf.urls import url
from . import views

urlpatterns = [
	# bv: /repertorium/
    url(r'^$', views.index, name='index'),
    # bv: /repertorium/decennium/1980
    url(r'^dec/(?P<decennium>[0-9]{4})$', views.decennium, name='decennium'),
    # bv: /repertorium/klas/123
    url(r'^klas/(?P<formaat>[wx])/(?P<klas_id>[0-9]+)$', views.klaslijst, name='klaslijst'),
    # bv: /repertorium/p/6677
    url(r'^p/(?P<persoon_id>[0-9]+)$', views.persoondetail, name='detail'),
    # bv: /repertorium/p/6677
    url(r'^az/(?P<letter>[a-zA-Z])$', views.az, name='az'),
    # bv: /repertorium/info
    url(r'^info$', views.info, name='info'),
    # rapporten
    url(r'^rapport$', views.rapport, name='rapport'),
    url(r'^rapport/(?P<formaat>[wx])/moetbetalen$', views.moetbetalen, name='moetbetalen'),
    url(r'^rapport/(?P<formaat>[wx])/vroegerbetaald/(?P<alle>[01])$', views.vroegerbetaald, name='vroegerbetaald'),
    url(r'^rapport/(?P<formaat>[wx])/ab$', views.moetABkrijgen, name='moetABkrijgen'),

    url(r'^rapport/(?P<formaat>[wx])/geenadres$', views.geenadres, name='geenadres'),
    url(r'^rapport/(?P<formaat>[wx])/mailinglijst$', views.mailinglijst, name='mailinglijst'),
    url(r'^rapport/(?P<formaat>[wx])/nietalumni$', views.nietalumni, name='nietalumni'),
]