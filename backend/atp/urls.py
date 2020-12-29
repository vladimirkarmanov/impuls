from django.urls import path

from .views import main, cluster_analysis

urlpatterns = [
    path('main/', main, name='main'),
    path('cluster/', cluster_analysis, name='cluster_analysis')
]
