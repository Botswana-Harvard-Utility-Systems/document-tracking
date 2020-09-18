from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin

from ..choices import DOC_TYPE, DOCUMENT_STATUS
from ..identifiers import DocumentIdentifier


class Document(BaseUuidModel, SiteModelMixin, models.Model):

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
        blank=True,
        null=False)

    doc_type = models.CharField(
        verbose_name="Document Type",
        max_length=10,
        choices=DOC_TYPE)

    file = models.FileField(upload_to='documents/')

    status = models.CharField(
        verbose_name="Document Status",
        max_length=20,
        choices=DOCUMENT_STATUS)

    send_to = models.CharField(
        verbose_name="Send Document To",
        max_length=35)

    def __str__(self):
        return f'{self.document_name}, {self.doc_type}, {self.doc_identifier}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.doc_identifier = self.identifier_cls().identifier
        super().save(*args, **kwargs)
