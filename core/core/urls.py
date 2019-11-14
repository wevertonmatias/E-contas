from django.contrib import admin
from django.urls import path, include
from E_contas import urls as econtas_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls), path('baton/', include('baton.urls')),
    path('econtas/', include(econtas_urls)),
] + static(settings.MEDIA_URL,
           doccument_root=settings.MEDIA_ROOT)

