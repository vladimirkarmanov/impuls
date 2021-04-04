from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config.views import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),

    path('register/', include(('register.urls', 'register'), namespace='register')),
    path('courses/', include(('courses.urls', 'courses'), namespace='courses')),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
