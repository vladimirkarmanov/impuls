from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include(('register.urls', 'register'), namespace='register')),
    path('events/', include(('events.urls', 'events'), namespace='events')),
    path('chats/', include(('chats.urls', 'chats'), namespace='chats')),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
