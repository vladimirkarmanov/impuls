import json

import pandas
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from atp.services import ClusterAnalysis


def main(request):
    context = {}
    if request.FILES.get('csvfile'):
        try:
            file = request.FILES['csvfile']
            dataset = pandas.read_csv(file)
            records = dataset.to_dict('records')
            students = [list(r.values()) for r in records]
            context['students'] = students
        except:
            context['error_msg'] = 'Невалидный файл!'
    return render(request, 'atp/main.html', context=context)


@csrf_exempt
def cluster_analysis(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        cluster_analyser = ClusterAnalysis()
        data = cluster_analyser.cluster_analysis(json_data)
        return JsonResponse(data)
