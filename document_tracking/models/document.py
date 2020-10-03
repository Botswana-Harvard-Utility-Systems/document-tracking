from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin

from ..identifiers import DocumentIdentifier


class Document(BaseUuidModel, SiteModelMixin, models.Model):

    identifier_cls = DocumentIdentifier

    document_name = models.CharField(
        verbose_name="Document Name",
        max_length=150,
        blank=False,
        null=True)

    file = models.FileField(null=True,
                            blank=True,
                            upload_to='documents/')

    def __str__(self):
        return f'{self.document_name}, {self.doc_identifier}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.doc_identifier = self.identifier_cls().identifier
        super().save(*args, **kwargs)
