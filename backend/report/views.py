import json
from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from register.models.TeacherRole import TeacherRole
from report.services.ClusterAnalysisService import ClusterAnalysisService


class IndexView(TemplateView):
    template_name = 'report/index.html'

    def post(self, request):
        context = {}
        try:
            # подгрузка из файла
            # filepath = os.path.join(settings.MEDIA_ROOT, 'data', 'students.csv')
            # dataset = pandas.read_csv(filepath)
            # records = dataset.to_dict('records')
            # students = [list(r.values()) for r in records]

            # из БД
            now_date = datetime.now().date()
            teachers = TeacherRole.objects.filter(date_end__gte=now_date, training_docs__isnull=False)
            students = []
            for teacher in teachers:
                student = [teacher.physical_face.get_surname_and_initials(),
                           teacher.academic_rank.name,
                           teacher.academic_degree.name,
                           teacher.qualification_category.name,
                           teacher.training_docs.last().date.year]
                students.append(student)

            context['students'] = students
        except Exception:
            context['error_msg'] = 'Ошибка загрузки'
        finally:
            return render(request, self.template_name, context=context)


@csrf_exempt
def analysis_process(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            cluster_analyser = ClusterAnalysisService()
            json_data = cluster_analyser.map_params(json_data, reverse=False)
            data = cluster_analyser.cluster_analysis(json_data)
            return JsonResponse(data)
        except Exception as exc:
            print(exc)
            data = {
                'error': 'Ошибка кластеризации, проверьте правильность данных.'
                         'Количество объектов кластеризации должно быть >= 5'
            }
            return JsonResponse(data)
