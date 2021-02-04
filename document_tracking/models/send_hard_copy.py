from datetime import date
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin

from bhp_personnel.models import Department, Employee
from .document import Document
from ..choices import DOCUMENT_STATUS, PRIORITY


class Courier(BaseUuidModel):

    full_name = models.CharField(
        verbose_name="Full name",
        max_length=150)

    cell = models.CharField(
        verbose_name='Cell number',
        max_length=50,
        blank=True,
        null=True,
        unique=True)

    email = models.EmailField(
        blank=True,
        null=True)

    def __str__(self):
        return f'{self.full_name}'


class SendHardCopy(BaseUuidModel, SiteModelMixin, models.Model):

    doc_identifier = models.CharField(
        verbose_name="Document Identifier",
        max_length=36,
        unique=True,
        null=True,
        blank=True)

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        related_name='department',
        null=True,
        blank=True)

    send_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True)

    reception = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        verbose_name='Reception',
        null=True,
        blank=True)

    recep_received = models.CharField(
        verbose_name='Personnel received at reception',
        max_length=100,
        blank=True,
        null=True)

    status = models.CharField(
        verbose_name="Status",
        max_length=20,
        blank=True,
        null=True,
        default='sent',
        choices=DOCUMENT_STATUS)

    priority = models.CharField(
        max_length=35,
        choices=PRIORITY,
        default='Normal')

    comment = models.TextField(
        verbose_name='Comments',
        blank=True,
        null=True,)

    sent_date = models.DateField(
        default=date.today)

    courier = models.CharField(
        verbose_name='Courier',
        max_length=20,
        blank=True,
        null=True)

    secondary_recep = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='destination_reception',
        verbose_name='Destination Reception',
        null=True,
        blank=True)

    handed_over = models.BooleanField(
        default=False,
        blank=True,
        null=True)

    secondary_recep_received = models.CharField(
        verbose_name='Personnel received at Secondary reception',
        max_length=100,
        blank=True,
        null=True)

    received_by = models.CharField(
        verbose_name='Received By',
        max_length=100,
        blank=True,
        null=True)

    class Meta:
        app_label = 'document_tracking'
        verbose_name = 'Send Hard Copies'
        verbose_name_plural = 'Send Hard Copies'
