from django import forms
from django.apps import apps as django_apps
from django.core.exceptions import ValidationError

from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidator, FormValidatorMixin

from ..models import Courier
from ..models import SendDocument


class SendDocumentFormValidator(FormValidator):

    document_model = 'document_tracking.document'

    @property
    def document_cls(self):
        return django_apps.get_model(self.document_model)

    def clean(self):
        super().clean()
        doc_identifier = self.cleaned_data.get('doc_identifier')
        send_to = self.cleaned_data.get('send_to')
        department = self.cleaned_data.get('department')
        courier = self.cleaned_data.get('courier')

        if not (send_to or department):
            message = {'department':
                       'Please select a department or personnel you '
                       'want to send this document to'}
            self._errors.update(message)
            raise ValidationError(message)
        else:
            pass

        try:
            document = self.document_cls.objects.get(
                doc_identifier=doc_identifier)
        except self.document_cls.DoesNotExist:
            raise ValidationError('Please complete the Document form first')
        else:
            if courier and document.document_form == 'soft_copy':
                message = {'courier':
                           'No need to specify a courier when sending '
                           'a soft-copy document'}
                self._errors.update(message)
                raise ValidationError(message)
            else:
                pass


class SendDocumentForm(SiteModelFormMixin, FormValidatorMixin,
                       forms.ModelForm):

    form_validator_cls = SendDocumentFormValidator

    doc_identifier = forms.CharField(
        required=False,
        label='Document Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = SendDocument
        fields = '__all__'


class CourierForm(forms.ModelForm):

    class Meta:
        model = Courier
        fields = '__all__'
