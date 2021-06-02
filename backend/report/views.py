import json
import os

import pandas
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from report.services.ClusterAnalysisService import ClusterAnalysisService


class IndexView(TemplateView):
    template_name = 'report/index.html'

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
        cluster_analyser = ClusterAnalysisService()
        json_data = cluster_analyser.map_params(json_data, reverse=False)
        data = cluster_analyser.cluster_analysis(json_data)
        return JsonResponse(data)
