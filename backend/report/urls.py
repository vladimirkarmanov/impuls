from django.urls import path

from .views import IndexView, analysis_process

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('analysis/', analysis_process, name='analysis_process'),
]
