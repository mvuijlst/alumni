from django.urls import include, re_path
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path('^', include('django.contrib.auth.urls')),
    re_path(r'^repertorium/', include('alumni.urls')),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', lambda r: HttpResponseRedirect('repertorium/')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
