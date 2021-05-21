import json
import os

import pandas
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, TemplateView

from core.cluster_analysis import ClusterAnalysis


def index(request):
    return render(request, 'qualification/index.html')


class CoursesList(ListView):
    pass


class Training(TemplateView):
    template_name = 'qualification/training.html'


class ChoiceOfEmployees(TemplateView):
    template_name = 'qualification/choice_of_employees.html'


class Analysis(TemplateView):
    template_name = 'qualification/analysis.html'

    def post(self, request):
        context = {}
        try:
            filepath = os.path.join(settings.MEDIA_ROOT, 'data', 'students.csv')
            dataset = pandas.read_csv(filepath)
            records = dataset.to_dict('records')
            students = [list(r.values()) for r in records]
            context['students'] = students
        except:
            context['error_msg'] = 'Невалидный файл!'
        finally:
            return render(request, self.template_name, context=context)


@csrf_exempt
def analysis_process(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        cluster_analyser = ClusterAnalysis()
        data = cluster_analyser.cluster_analysis(json_data)
        return JsonResponse(data)
