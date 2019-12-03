from django.urls import path, re_path

from .views import (ListenerSignupView, UserLoginView,
                    UserLogoutView, AdditionalInfoView, activate_account)

urlpatterns = [
    path('signup/', ListenerSignupView.as_view(), name='listener_signup_url'),
    re_path('^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            activate_account, name='activate_account_url'),
    path('signup/paper', AdditionalInfoView.as_view(), name='additional_info_url'),
    path('login/', UserLoginView.as_view(), name='user_login_url'),
    path('logout/', UserLogoutView.as_view(), name='user_logout_url')
]
