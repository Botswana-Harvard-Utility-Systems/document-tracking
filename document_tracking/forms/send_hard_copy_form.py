from django import forms
from django.core.exceptions import ValidationError

from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidator, FormValidatorMixin

from ..models import Courier
from ..models import SendHardCopy


class SendHardCopyFormValidator(FormValidator):

    def clean(self):

        reception = self.cleaned_data.get('reception')
        secondary_recep = self.cleaned_data.get('secondary_recep')

        if reception and not secondary_recep:
            message = {'reception':
                       'Please specify destination reception'}
            self._errors.update(message)
            raise ValidationError(message)


class SendHardCopyForm(SiteModelFormMixin, FormValidatorMixin,
                       forms.ModelForm):

    form_validator_cls = SendHardCopyFormValidator

    doc_identifier = forms.CharField(
        required=False,
        label='Document Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    recep_received = forms.CharField(
        required=False,
        label='Receiver At Reception',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    handed_over = forms.CharField(
        required=False,
        label='Handed-Over',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    secondary_recep_received = forms.CharField(
        required=False,
        label='Secondary Reception Receiver',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    received_by = forms.CharField(
        required=False,
        label='Receiver At Destination',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    courier = forms.CharField(
        required=False,
        label='Courier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    user_created_disabled_fields = ['courier']
    bhp_hq_disabled_fields = ['department', 'send_to', 'reception',
                              'priority']
    other_fields = ['department', 'send_to', 'reception', 'comment',
                    'priority', 'courier', 'secondary_recep']

    class Meta:
        model = SendHardCopy
        fields = '__all__'


class CourierForm(forms.ModelForm):

    class Meta:
        model = Courier
        fields = '__all__'
