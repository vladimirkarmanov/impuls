from django.contrib import admin
from django.contrib.auth.models import Group

from .models import JobPosition, EducationalOrganization, EducationalDocument

admin.site.unregister(Group)


@admin.register(JobPosition)
class JobPositionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

    class Meta:
        model = JobPosition


@admin.register(EducationalOrganization)
class EducationalOrganizationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

    class Meta:
        model = EducationalOrganization


@admin.register(EducationalDocument)
class EducationalDocumentAdmin(admin.ModelAdmin):
    list_display = ('number',)
    list_display_links = ('number',)
    search_fields = ('number',)

    class Meta:
        model = EducationalDocument
