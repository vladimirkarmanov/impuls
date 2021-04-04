from django.shortcuts import render
from django.views.generic import ListView, TemplateView


def index(request):
    return render(request, 'courses/index.html')


class CoursesList(ListView):
    pass


class Training(TemplateView):
    template_name = 'courses/training.html'


class ChoiceOfEmployees(TemplateView):
    template_name = 'courses/choice_of_employees.html'
