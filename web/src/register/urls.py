from django.urls import path, re_path

from .views import (ListenerSignupView,
                    UserLoginView,
                    UserLogoutView,
                    AdditionalInfoView,
                    activate_account,
                    UserPasswordResetView,
                    UserPasswordResetConfirmView,
                    UserPasswordResetCompleteView,
                    UserPasswordResetDoneView,
                    UserPasswordChangeView,
                    UserPasswordChangeDoneView)

urlpatterns = [
    path('signup/', ListenerSignupView.as_view(), name='listener_signup'),
    path('signup/paper/', AdditionalInfoView.as_view(), name='additional_info'),

    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),

    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            activate_account, name='activate_account'),

    path('password_reset/', UserPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'^password_reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_change/', UserPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', UserPasswordChangeDoneView.as_view(), name='password_change_done')
]
