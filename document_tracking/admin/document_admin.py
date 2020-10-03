from django.contrib import admin

from edc_model_admin import audit_fieldset_tuple

from ..admin_site import document_tracking_admin
from ..forms import DocumentForm
from ..models import Document

from .modeladmin_mixins import ModelAdminMixin


@admin.register(Document, site=document_tracking_admin)
class DocumentAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = DocumentForm
    search_fields = ['doc_identifier']

    fieldsets = (
        (None, {
            'fields': (
                'doc_identifier',
                'document_name',
                'file')}),
        audit_fieldset_tuple)
