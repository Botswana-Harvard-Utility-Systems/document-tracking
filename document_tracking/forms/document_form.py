from django import forms

from django.core.exceptions import ValidationError
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidator, FormValidatorMixin

from ..models import Document


class DocumentFormValidator(FormValidator):

    def clean(self):
        super().clean()

        file = self.cleaned_data.get('file')
        document_form = self.cleaned_data.get('document_form')

        if document_form in ['soft_copy', 'both'] and not file:
            message = {'file':
                       'Please Upload file'}
            self._errors.update(message)
            raise ValidationError(message)

        if document_form == 'hard_copy' and file:
            message = {'file':
                       'soft-copy file not required'}
            self._errors.update(message)
            raise ValidationError(message)
        else:
            pass

        self.validate_other_specify(
            'document_type',
            other_specify_field='document_type_other')


class DocumentForm(SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):

    form_validator_cls = DocumentFormValidator

    doc_identifier = forms.CharField(
        required=False,
        label='Document Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Document
        fields = '__all__'
