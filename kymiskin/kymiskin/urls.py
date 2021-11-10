#cridad/settings.py

from django.contrib import admin
from django.urls import path, include
from kymiskin import settings
from django.conf.urls import url

from website import views

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('', include("django.contrib.auth.urls")),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

