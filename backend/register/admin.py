from django.contrib import admin
from django.contrib.auth.models import Group

from register.models.AcademicDegree import AcademicDegree
from register.models.AcademicRank import AcademicRank
from register.models.Contact import Contact
from register.models.ContactType import ContactType
from register.models.EducationType import EducationType
from register.models.EducationalDocument import EducationalDocument
from register.models.EducationalOrganization import EducationalOrganization
from register.models.JobPosition import JobPosition
from register.models.PhysicalFace import PhysicalFace
from register.models.QualificationCategory import QualificationCategory
from register.models.TeacherRole import TeacherRole

admin.site.unregister(Group)


@admin.register(AcademicDegree)
class AcademicDegreeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

    class Meta:
        model = AcademicDegree


@admin.register(AcademicRank)
class AcademicRankAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

    class Meta:
        model = AcademicRank


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('contact_number',)
    list_display_links = ('contact_number',)
    search_fields = ('contact_number',)

    class Meta:
        model = Contact


@admin.register(ContactType)
class ContactTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

    class Meta:
        model = ContactType


@admin.register(EducationalDocument)
class EducationalDocumentAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
    search_fields = ('id',)

    class Meta:
        model = EducationalDocument


@admin.register(EducationalOrganization)
class EducationalOrganizationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

    class Meta:
        model = EducationalOrganization


@admin.register(EducationType)
class EducationTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

    class Meta:
        model = EducationType


@admin.register(JobPosition)
class JobPositionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

    class Meta:
        model = JobPosition


@admin.register(QualificationCategory)
class QualificationCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

    class Meta:
        model = QualificationCategory


@admin.register(TeacherRole)
class TeacherRoleAdmin(admin.ModelAdmin):
    list_display = ('date_start',)
    list_display_links = ('date_start',)
    search_fields = ('date_start',)

    class Meta:
        model = TeacherRole


@admin.register(PhysicalFace)
class PhysicalFaceAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'patronymic')
    list_display_links = ('first_name',)
    search_fields = ('first_name', 'last_name', 'patronymic')

    class Meta:
        model = PhysicalFace
