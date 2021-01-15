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
        verbose_name='Sent date',
        default=date.today,
        blank=True,
        null=True,)

    courier = models.ForeignKey(
        Courier,
        blank=True,
        null=True,
        on_delete=models.CASCADE)

    secondary_recep = models.ForeignKey(
        Group,
        related_name='secondary_recep',
        on_delete=models.SET_NULL,
        verbose_name='Reception',
        null=True,
        blank=True)

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

    def get_sent_to(self):
        sent_to_list = ''
        for sent_to in self.send_to.all():
            sent_to_list = sent_to_list + sent_to.username + ','
        return sent_to_list[:-1]

    class Meta:
        app_label = 'document_tracking'
        verbose_name = 'Send Hard Copies'
        verbose_name_plural = 'Send Hard Copies'
