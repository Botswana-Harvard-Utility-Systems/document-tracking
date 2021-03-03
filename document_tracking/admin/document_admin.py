from django.contrib import admin
from django.contrib.auth import get_user

from edc_model_admin import audit_fieldset_tuple

from ..admin_site import document_tracking_admin
from ..forms import DocumentForm
from ..models import Document

from .modeladmin_mixins import ModelAdminMixin


@admin.register(Document, site=document_tracking_admin)
class DocumentAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = DocumentForm
    search_fields = ['doc_identifier', 'document_name', 'document_type',
                     'document_type_other']

    fieldsets = (
        (None, {
            'fields': (
                'doc_identifier',
                'document_name',
                'file',
                'document_type',
                'document_type_other',
                'document_form',)}),
        audit_fieldset_tuple)

    radio_fields = {
        'document_type': admin.VERTICAL,
    }

    def has_change_permission(self, request, obj=None):
        user_created = obj.user_created if obj else None
        if user_created and user_created != get_user(request).username:
            return False
        return True

