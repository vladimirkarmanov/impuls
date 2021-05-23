from django.views.generic import ListView

from qualification.models.Course import Course


class IndexView(ListView):
    model = Course
    template_name = 'qualification/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context
