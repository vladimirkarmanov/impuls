from django.contrib import admin

from qualification.models.Course import Course
from qualification.models.DistributionPerCourse import DistributionPerCourse
from qualification.models.SessionAttendance import SessionAttendance
from qualification.models.TrainingDocument import TrainingDocument
from qualification.models.TrainingRequest import TrainingRequest


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name')
    list_display_links = ('name',)
    search_fields = ('name',)

    class Meta:
        model = Course


@admin.register(DistributionPerCourse)
class DistributionPerCourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_start', 'date_end', 'course')
    list_display_links = ('id',)
    search_fields = ('id',)

    class Meta:
        model = DistributionPerCourse


@admin.register(SessionAttendance)
class SessionAttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'date')
    list_display_links = ('date',)
    search_fields = ('date',)

    class Meta:
        model = SessionAttendance


@admin.register(TrainingDocument)
class SessionAttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'number_of_hours')
    list_display_links = ('id',)
    search_fields = ('id',)

    class Meta:
        model = TrainingDocument


@admin.register(TrainingRequest)
class SessionAttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'date')
    list_display_links = ('id',)
    search_fields = ('id',)

    class Meta:
        model = TrainingRequest
