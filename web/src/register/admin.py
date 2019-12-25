from typing import List

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.db.models import QuerySet

from .models import User, AdditionalUserInfo, JobPlace, JobPosition


@admin.register(JobPosition)
class JobPositionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

    class Meta:
        model = JobPosition


@admin.register(JobPlace)
class JobPlaceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

    class Meta:
        model = JobPlace


class AdditionalUserInfoInline(admin.StackedInline):
    model = AdditionalUserInfo


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    inlines = (AdditionalUserInfoInline,)
    list_display = ('get_full_name', 'username', 'email', 'get_user_groups',
                    'is_staff')
    list_display_links = ('username',)

    readonly_fields = ('date_joined', 'last_login', 'is_superuser')
    fieldsets = (
        ('Личные данные', {'fields': ('first_name',
                                      'last_name',
                                      'patronymic',
                                      'username',
                                      'email',
                                      'password')}),
        ('Работа', {'fields': ('experience',
                               'job_place',
                               'job_position')}),
        ('Служебная информация', {'fields': ('date_joined',
                                             'last_login',
                                             'is_superuser')})
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Личные данные', {'fields': ('first_name',
                                      'last_name',
                                      'patronymic',
                                      'email')}),
        ('Работа', {'fields': ('experience',
                               'job_place',
                               'job_position')}),
        ('Служебная информация', {'fields': ('date_joined',
                                             'last_login',
                                             'is_superuser')})
    )

    def get_full_name(self, obj) -> str:
        return obj.get_full_name()

    def get_user_groups(self, obj) -> List[str]:
        return [group.name for group in obj.groups.all()]

    get_full_name.short_description = 'ФИО'
    get_user_groups.short_description = 'Группы'

    def save_model(self, request, obj, form, change) -> None:
        obj.save()
        obj.add_user_to_group_teachers()
        super().save_model(request, obj, form, change)

    def get_queryset(self, request) -> QuerySet:
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            return queryset.filter(is_superuser=False)
        return queryset

    class Meta:
        model = User


admin.site.unregister(Group)
