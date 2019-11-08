from django.contrib import admin
from django.urls import path, include

from .views import ListenerSignupView

urlpatterns = [
    path('signup/', ListenerSignupView.as_view(), name='listener_signup_url')
]
