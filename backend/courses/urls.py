from django.urls import path

from courses.views import CoursesList, index, Training, ChoiceOfEmployees

urlpatterns = [
    path('', index, name='index'),
    path('list/', CoursesList.as_view(), name='courses_list'),
    path('training/', Training.as_view(), name='training'),
    path('choice/', ChoiceOfEmployees.as_view(), name='choice'),
]
