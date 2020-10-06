from datetime import date
from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin

from bhp_personnel.models import Department, Employee
from ..choices import DOCUMENT_STATUS


class SendDocument(BaseUuidModel, SiteModelMixin, models.Model):

    doc_identifier = models.CharField(
        verbose_name="Document Identifier",
        max_length=36,
        null=True,
        blank=True,
        unique=True)

    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    send_to = models.ForeignKey(Employee, on_delete=models.CASCADE)

    status = models.CharField(
        verbose_name="Status",
        max_length=20,
        blank=True,
        null=True,
        choices=DOCUMENT_STATUS)

    action_priority = models.CharField(
        max_length=35,
        choices=(('normal', 'Normal'), ('Medium', 'Medium'), ('high', 'High')),
        default='Normal')

    comment = models.TextField(
        verbose_name='Comments',
        blank=True,
        null=True,)

    action_date = models.DateField(
        verbose_name='Action date',
        default=date.today, )
