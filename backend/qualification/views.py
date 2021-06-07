from django.views.generic import ListView, TemplateView

from qualification.models.Course import Course
from qualification.models.DistributionPerCourse import DistributionPerCourse
from qualification.models.TrainingRequest import TrainingRequest


class IndexView(ListView):
    model = Course
    template_name = 'qualification/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context


class TrainingView(TemplateView):
    template_name = 'qualification/training.html'


class RequestsList(ListView):
    model = TrainingRequest
    template_name = 'qualification/requests.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requests'] = TrainingRequest.objects.all()
        return context


class DistributionsList(ListView):
    model = DistributionPerCourse
    template_name = 'qualification/distributions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['distributions'] = DistributionPerCourse.objects.all()
        return context
