from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config.views import index

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('register/', include(('register.urls', 'register'), namespace='register')),
    path('events/', include(('events.urls', 'events'), namespace='events')),
    path('atp/', include(('atp.urls', 'atp'), namespace='atp'))
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
