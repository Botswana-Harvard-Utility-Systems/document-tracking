from django import forms

from django.core.exceptions import ValidationError
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidator, FormValidatorMixin

from ..models import HardCopyDocument


class HardCopyDocumentForm(SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):

    doc_identifier = forms.CharField(
        required=False,
        label='Document Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = HardCopyDocument
        fields = '__all__'
