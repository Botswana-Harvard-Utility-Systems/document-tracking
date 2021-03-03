from django.contrib import admin
from django.contrib.auth import get_user
from django.contrib.auth.models import User

from edc_model_admin import audit_fieldset_tuple

from ..admin_site import document_tracking_admin
from ..forms import CourierForm, SendDocumentForm
from ..models import Courier, SendDocument

from .modeladmin_mixins import ModelAdminMixin

from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter


@admin.register(SendDocument, site=document_tracking_admin)
class SendDocumentAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = SendDocumentForm
    search_fields = ['doc_identifier']

    fieldsets = (
        (None, {
            'fields': (
                'doc_identifier',
                'transaction_identifier',
                'department',
                'send_to',
                'priority',
                'comment',
                'sent_date',
                'group',)}),
        audit_fieldset_tuple)

    radio_fields = {
        # "department": admin.VERTICAL,
        "priority": admin.VERTICAL,
    }

    # autocomplete_fields = ['department']

    filter_horizontal = ('send_to', 'group', 'department')

    list_filter = (
        ('department', RelatedDropdownFilter),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super(SendDocumentAdmin, self).get_form(request, obj, **kwargs)
        form.request = request
        return form
