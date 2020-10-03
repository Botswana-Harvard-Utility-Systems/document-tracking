from django.contrib import admin

from edc_model_admin import audit_fieldset_tuple

from ..admin_site import document_tracking_admin
from ..forms import SendDocumentForm
from ..models import SendDocument

from .modeladmin_mixins import ModelAdminMixin


@admin.register(SendDocument, site=document_tracking_admin)
class SendDocumentAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = SendDocumentForm
    search_fields = ['doc_identifier']

    fieldsets = (
        (None, {
            'fields': (
                'doc_identifier',
                'department',
                'send_to',
                'status',
                'action_priority',
                'comment',
                'action_date')}),
        audit_fieldset_tuple)
