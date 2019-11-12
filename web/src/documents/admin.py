from django.contrib import admin

from .models import Document, DocumentType, DocumentRegulation, Contract


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('number', 'file', 'user', 'document_type')
    list_display_links = ('number',)
    search_fields = ('number',)

    class Meta:
        model = Document


@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'event', 'get_documents')
    list_display_links = ('name',)
    list_filter = ('event',)
    search_fields = ('name',)

    def get_documents(self, obj):
        documents = Document.objects.filter(document_type=obj)
        return ' | '.join(str(document) for document in documents)

    get_documents.short_description = 'Документы'

    class Meta:
        model = DocumentType


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('number', 'status', 'start_date',
                    'end_date', 'document_regulation', 'user')
    list_display_links = ('number',)
    list_filter = ('start_date', 'end_date', 'status')
    search_fields = ('number',)

    class Meta:
        model = Contract


@admin.register(DocumentRegulation)
class DocumentRegulationAdmin(admin.ModelAdmin):
    list_display = ('document_type', 'get_contracts')
    list_display_links = ('document_type',)
    search_fields = ('document_type',)

    def get_contracts(self, obj):
        contracts = Contract.objects.filter(document_regulation=obj)
        return ' | '.join(str(contract) for contract in contracts)

    get_contracts.short_description = 'Договоры'

    class Meta:
        model = DocumentRegulation
