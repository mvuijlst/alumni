from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^repertorium/', include('alumni.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', lambda r: HttpResponseRedirect('repertorium/')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)