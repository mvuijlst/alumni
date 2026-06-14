from django.urls import re_path
from . import views

urlpatterns = [
	# bv: /repertorium/
    re_path(r'^$', views.index, name='index'),
    # bv: /repertorium/decennium/1980
    re_path(r'^dec/(?P<decennium>[0-9]{4})$', views.decennium, name='decennium'),
    # bv: /repertorium/klas/123
    re_path(r'^klas/(?P<formaat>[wx])/(?P<klas_id>[0-9]+)$', views.klaslijst, name='klaslijst'),
    # bv: /repertorium/p/6677
    re_path(r'^p/(?P<persoon_id>[0-9]+)$', views.persoondetail, name='detail'),
    # bv: /repertorium/p/6677
    re_path(r'^az/(?P<letter>[a-zA-Z])$', views.az, name='az'),
    # bv: /repertorium/info
    re_path(r'^info$', views.info, name='info'),
    # rapporten
    re_path(r'^rapport$', views.rapport, name='rapport'),
    re_path(r'^rapport/(?P<formaat>[wx])/moetbetalen$', views.moetbetalen, name='moetbetalen'),
    re_path(r'^rapport/(?P<formaat>[wx])/vroegerbetaald/(?P<alle>[01])$', views.vroegerbetaald, name='vroegerbetaald'),
    re_path(r'^rapport/(?P<formaat>[wx])/ab$', views.moetABkrijgen, name='moetABkrijgen'),

    re_path(r'^rapport/(?P<formaat>[wx])/geenadres$', views.geenadres, name='geenadres'),
    re_path(r'^rapport/(?P<formaat>[wx])/mailinglijst$', views.mailinglijst, name='mailinglijst'),
    re_path(r'^rapport/(?P<formaat>[wx])/linkedin$', views.linkedin, name='linkedin'),
    re_path(r'^rapport/(?P<formaat>[wx])/nietalumni$', views.nietalumni, name='nietalumni'),
    
    re_path(r'^rapport/fotomuur$', views.fotomuur, name='fotomuur'),
    re_path(r'^rapport/wikipedia$', views.wikipedia, name='wikipedia'),
]
