from django.contrib import admin

from .models import TrainingDocument


@admin.register(TrainingDocument)
class TrainingDocumentAdmin(admin.ModelAdmin):
    list_display = ('number',)
    list_display_links = ('number',)
    search_fields = ('number', 'date')

    class Meta:
        model = TrainingDocument
