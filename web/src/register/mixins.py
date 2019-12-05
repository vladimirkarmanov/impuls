from django.shortcuts import redirect, reverse
from django.contrib.auth.mixins import AccessMixin


class UserAlreadyAuthenticatedMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')

        return super().dispatch(request, *args, **kwargs)
