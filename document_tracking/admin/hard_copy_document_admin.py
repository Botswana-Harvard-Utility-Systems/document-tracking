from django.contrib import admin
from django.contrib.auth import get_user

from edc_model_admin import audit_fieldset_tuple

from ..admin_site import document_tracking_admin
from ..forms import HardCopyDocumentForm
from ..models import HardCopyDocument

from .modeladmin_mixins import ModelAdminMixin


@admin.register(HardCopyDocument, site=document_tracking_admin)
class HardCopyDocumentAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = HardCopyDocumentForm
    search_fields = ['doc_identifier']

    fieldsets = (
        (None, {
            'fields': (
                'doc_identifier',
                'document_name',
                'document_type',
                'document_type_other',)}),
        audit_fieldset_tuple)

    radio_fields = {
        'document_type': admin.VERTICAL,
    }

    def has_change_permission(self, request, obj=None):
        user_created = obj.user_created if obj else None
        if user_created and user_created != get_user(request).username:
            return False
        return True
