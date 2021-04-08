from django.contrib import admin

from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'short_name')
    list_display_links = ('name',)
    search_fields = ('name',)

    class Meta:
        model = Course
