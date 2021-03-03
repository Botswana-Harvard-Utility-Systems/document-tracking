from django.contrib import admin
from django.contrib.auth import get_user
from django.contrib.auth.models import User

from edc_model_admin import audit_fieldset_tuple

from ..admin_site import document_tracking_admin
from ..forms import CourierForm, SendHardCopyForm
from ..models import Courier, SendHardCopy

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


@admin.register(SendHardCopy, site=document_tracking_admin)
class SendHardCopyAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = SendHardCopyForm
    search_fields = ['doc_identifier', 'status', 'recep_received', 'comment',
                     'courier', 'received_by']

    fieldsets = (
        (None, {
            'fields': (
                'doc_identifier',
                'department',
                'send_to',
                'reception',
                'priority',
                'comment',
                'courier',
                'secondary_recep',
                'handed_over',
                'secondary_recep_received',
                'received_by',)}),
        audit_fieldset_tuple)

    radio_fields = {
        "reception": admin.VERTICAL,
        "secondary_recep": admin.VERTICAL,
        "priority": admin.VERTICAL,
    }

    # autocomplete_fields = ['department']

    list_filter = (
        ('department', RelatedDropdownFilter),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super(SendHardCopyAdmin, self).get_form(request, obj, **kwargs)
        form.request = request
        return form
