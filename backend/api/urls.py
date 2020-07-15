from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import user_list

urlpatterns = [
    path('users/', login_required(user_list), name='user_list')
]
