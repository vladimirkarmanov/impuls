from django.urls import path

from courses.views import CoursesList, index, Training, ChoiceOfEmployees, Analysis, analysis_process

urlpatterns = [
    path('', index, name='index'),
    path('list/', CoursesList.as_view(), name='courses_list'),
    path('training/', Training.as_view(), name='training'),
    path('choice/', ChoiceOfEmployees.as_view(), name='choice'),
    path('analysis/', Analysis.as_view(), name='analysis'),
    path('analysis/process', analysis_process, name='analysis_process'),
]
