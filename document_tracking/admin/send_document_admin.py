from django.contrib import admin

from edc_model_admin import audit_fieldset_tuple

from ..admin_site import document_tracking_admin
from ..forms import CourierForm, SendDocumentForm
from ..models import Courier, SendDocument

from .modeladmin_mixins import ModelAdminMixin

from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter


@admin.register(Courier, site=document_tracking_admin)
class CourierAdmin(
        ModelAdminMixin, admin.ModelAdmin):

    form = CourierForm

    fieldsets = (
        (None, {
            'fields': (
                'full_name',
                'cell',
                'email',
            )}),
        audit_fieldset_tuple)

    search_fields = ['full_name', 'cell', 'email',]


@admin.register(SendDocument, site=document_tracking_admin)
class SendDocumentAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = SendDocumentForm
    search_fields = ['doc_identifier']

    fieldsets = (
        (None, {
            'fields': (
                'doc_identifier',
                'document',
                'department',
                'send_to',
                'courier',
                'final_destination',
                'receiver_at_destination',
                'status',
                'action_priority',
                'comment',
                'action_date')}),
        audit_fieldset_tuple)

    radio_fields = {
        # "department": admin.VERTICAL,
        "status": admin.VERTICAL,
        "action_priority": admin.VERTICAL,
    }

    # autocomplete_fields = ['department']

    list_filter = (
        ('department', RelatedDropdownFilter),
    )
