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


class SendDocument(BaseUuidModel, SiteModelMixin, models.Model):

    doc_identifier = models.CharField(
        verbose_name="Document Identifier",
        max_length=36,
        null=True,
        blank=True)

    department = models.ManyToManyField(
        Department,
        related_name='document',
        blank=True)

    send_to = models.ManyToManyField(
        User,
        blank=True)

    status = models.CharField(
        verbose_name="Status",
        max_length=20,
        choices=DOCUMENT_STATUS)

    action_priority = models.CharField(
        max_length=35,
        choices=PRIORITY,
        default='Normal')

    comment = models.TextField(
        verbose_name='Comments',
        blank=True,
        null=True,)

    action_date = models.DateField(
        verbose_name='Action date',
        default=date.today,
        blank=True,
        null=True,
    )

    group = models.ManyToManyField(
        Group,
        verbose_name='Group of people that can view this document')

    courier = models.ForeignKey(
        Courier,
        blank=True,
        null=True,
        on_delete=models.CASCADE)

    final_destination = models.ManyToManyField(
        Department,
        blank=True,)

    receiver_at_destination = models.ManyToManyField(
        User,
        blank=True,
        related_name='user',)

    class Meta:
        unique_together = ['doc_identifier',]
