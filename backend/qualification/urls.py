from django.urls import path

from .views import IndexView, TrainingView, RequestsList, DistributionsList

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('training/', TrainingView.as_view(), name='training'),
    path('requests/', RequestsList.as_view(), name='requests_list'),
    path('distributions/', DistributionsList.as_view(), name='distributions_list')
]
