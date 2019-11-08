from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'username', 'email', 'get_user_groups')
    list_display_links = ('username',)
    search_fields = ('username',)

    def get_full_name(self, obj):
        return f'{obj.first_name} {obj.last_name} {obj.patronymic}'

    def get_user_groups(self, obj):
        groups = Group.objects.all()
        return [group.name for group in groups if obj in group.user_set.all()]

    get_full_name.short_description = 'ФИО'
    get_user_groups.short_description = 'Группа'

    class Meta:
        model = User
