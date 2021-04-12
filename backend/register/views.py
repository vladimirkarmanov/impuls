from django.contrib.auth.views import (LoginView,
                                       LogoutView)
from django.utils.decorators import method_decorator

from core.decorators import login_not_required
from .forms import (UserLoginForm)
from .mixins import UserAlreadyAuthenticatedMixin


@method_decorator(login_not_required, name='dispatch')
class UserLoginView(UserAlreadyAuthenticatedMixin, LoginView):
    authentication_form = UserLoginForm
    template_name = 'register/login_form.html'


@method_decorator(login_not_required, name='dispatch')
class UserLogoutView(LogoutView):
    pass
