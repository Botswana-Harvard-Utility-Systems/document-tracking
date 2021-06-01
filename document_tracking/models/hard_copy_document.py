from django.db import models

from edc_base.model_fields import OtherCharField
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin

from ..choices import DOCUMENT_FORM, DOCUMENT_TYPE
from ..identifiers import DocumentIdentifier


class HardCopyDocument(BaseUuidModel, SiteModelMixin, models.Model):

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
        null=False,
        choices=DOCUMENT_FORM)

    def __str__(self):
        return f'{self.document_name}, {self.doc_identifier}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.doc_identifier = self.identifier_cls().identifier
            self.document_form = 'hard_copy'
        super().save(*args, **kwargs)
