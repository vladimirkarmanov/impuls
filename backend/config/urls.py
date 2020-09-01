from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from register.views import JobPlaceViewSet, JobPositionViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Impuls API",
        default_version='v1',
        description="REST API"
    ),
    public=False,
    permission_classes=(permissions.IsAdminUser,),
)

router = routers.DefaultRouter()
router.register('job-places', JobPlaceViewSet)
router.register('job-positions', JobPositionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('admin/', admin.site.urls),
    path('api/', include(('api.urls', 'api'), namespace='api')),
    path('register/', include(('register.urls', 'register'), namespace='register')),
    path('events/', include(('events.urls', 'events'), namespace='events')),
    path('chats/', include(('chats.urls', 'chats'), namespace='chats')),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
