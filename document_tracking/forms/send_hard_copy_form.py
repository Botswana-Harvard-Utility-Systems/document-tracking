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

    # def check_user(self):
    #
    #     if self.instance.user_created != self.request.user:
    #         doc_identifier = forms.CharField(
    #             required=False,
    #             label='Document Identifier',
    #             widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    disabled_fields = ['status']

    class Meta:
        model = SendHardCopy
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        super(SendHardCopyForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)

        if instance.user_created == self.request.user.username:
            for field in self.disabled_fields:
                self.fields[field].disabled = True
        else:
            pass


class CourierForm(forms.ModelForm):

    class Meta:
        model = Courier
        fields = '__all__'
