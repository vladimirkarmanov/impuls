from django.contrib.auth.views import LoginView, LogoutView
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from core.decorators import login_not_required
from register.models.TeacherRole import TeacherRole
from .forms import UserLoginForm
from .mixins import UserAlreadyAuthenticatedMixin


@method_decorator(login_not_required, name='dispatch')
class UserLoginView(UserAlreadyAuthenticatedMixin, LoginView):
    authentication_form = UserLoginForm
    template_name = 'register/login_form.html'


@method_decorator(login_not_required, name='dispatch')
class UserLogoutView(LogoutView):
    pass


class StudentsList(ListView):
    model = TeacherRole
    template_name = 'register/students_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = TeacherRole.objects.all()
        return context
