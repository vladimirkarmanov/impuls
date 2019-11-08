from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ListenerSignUpForm
from .models import User


class ListenerSignupView(CreateView):
    model = User
    form_class = ListenerSignUpForm
    template_name = 'register/signup_form.html'
    success_url = reverse_lazy('listener_signup_url')
