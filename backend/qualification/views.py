from django.shortcuts import render
from django.views.generic import ListView, TemplateView


def index(request):
    return render(request, 'qualification/index.html')


class CoursesList(ListView):
    pass


class Training(TemplateView):
    template_name = 'qualification/training.html'


class ChoiceOfEmployees(TemplateView):
    template_name = 'qualification/choice_of_employees.html'
