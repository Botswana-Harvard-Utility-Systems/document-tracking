from django import forms

from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidator, FormValidatorMixin

from ..models import Courier
from ..models import SendHardCopy


class SendHardCopyForm(SiteModelFormMixin, FormValidatorMixin,
                       forms.ModelForm):

    doc_identifier = forms.CharField(
        required=False,
        label='Document Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    recep_received = forms.CharField(
        required=False,
        label='Receiver At Reception',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    secondary_recep_received = forms.CharField(
        required=False,
        label='Secondary Reception Receiver',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    received_by = forms.CharField(
        required=False,
        label='Receiver At Destination',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    user_created_disabled_fields = ['status', 'courier', 'secondary_recep']
    bhp_hq_disabled_fields = ['department', 'send_to', 'reception', 'status',
                              'priority', 'sent_date']
    other_fields = ['department', 'send_to', 'reception', 'status', 'comment',
                    'priority', 'sent_date', 'courier', 'secondary_recep']

    class Meta:
        model = SendHardCopy
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        super(SendHardCopyForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)

        if instance.user_created == self.request.user.username:
            for field in self.user_created_disabled_fields:
                self.fields[field].disabled = True

        elif self.request.user.groups.filter(name='BHP HQ').exists():
            for field in self.bhp_hq_disabled_fields:
                self.fields[field].disabled = True

        elif instance.received_by == self.request.user.username:
            for field in self.other_fields:
                self.fields[field].disabled = True

        else:
            pass


class CourierForm(forms.ModelForm):

    class Meta:
        model = Courier
        fields = '__all__'
