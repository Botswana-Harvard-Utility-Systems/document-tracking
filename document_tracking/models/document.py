from django.db import models

from edc_base.model_fields import OtherCharField
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_search.model_mixins import SearchSlugModelMixin

from ..choices import DOCUMENT_TYPE
from ..identifiers import DocumentIdentifier


class Document(BaseUuidModel, SearchSlugModelMixin,
               SiteModelMixin, models.Model):

    identifier_cls = DocumentIdentifier

    doc_identifier = models.CharField(
        verbose_name="Document Identifier",
        max_length=36,
        null=True,
        blank=True,
        unique=True)

    document_name = models.CharField(
        verbose_name="Document Name",
        max_length=150,
        blank=False,
        null=True)

    file = models.FileField(null=True,
                            blank=True,
                            upload_to='documents/')

    document_type = models.CharField(
        verbose_name="Document Type",
        max_length=150,
        blank=False,
        null=True,
        choices=DOCUMENT_TYPE)

    document_type_other = OtherCharField()

    document_form = models.CharField(
        verbose_name="Document Form",
        max_length=150,
        blank=False,
        null=False)

    def __str__(self):
        return f'{self.document_name}, {self.doc_identifier}'

    def get_search_slug_fields(self):
        fields = super().get_search_slug_fields()
        fields.append('doc_identifier')
        fields.append('document_name')
        fields.append('document_type')
        fields.append('document_type_other')
        return fields

    def save(self, *args, **kwargs):
        if not self.id:
            self.doc_identifier = self.identifier_cls().identifier
        super().save(*args, **kwargs)
