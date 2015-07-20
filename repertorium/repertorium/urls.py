from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponseRedirect

urlpatterns = [
    url(r'^repertorium/', include('alumni.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', lambda r: HttpResponseRedirect('repertorium/')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
       {'template_name': 'admin/login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
]
