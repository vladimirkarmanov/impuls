from django.urls import path

from .views import ListenerSignupView, UserLoginView, UserLogoutView

urlpatterns = [
    path('signup/', ListenerSignupView.as_view(), name='listener_signup_url'),
    path('login/', UserLoginView.as_view(), name='user_login_url'),
    path('logout/', UserLogoutView.as_view(), name='user_logout_url')
]
