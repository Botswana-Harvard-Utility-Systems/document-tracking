from django import forms

from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin

from ..models import SendDocument


class SendDocumentForm(SiteModelFormMixin, FormValidatorMixin,
                       forms.ModelForm):

    doc_identifier = forms.CharField(
        required=False,
        label='Document Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = SendDocument
        fields = '__all__'
