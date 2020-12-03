from datetime import date
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin

from bhp_personnel.models import Department, Employee
from .document import Document
from ..choices import DOCUMENT_STATUS


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
        blank=True,
        unique=True)

    group = models.ForeignKey(
        Group,
        verbose_name='Choose Group',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text='Group of people that can view this document')

    department = models.ForeignKey(
        Department,
        related_name='document',
        on_delete=models.CASCADE)

    send_to = models.ForeignKey(User, on_delete=models.CASCADE)

    courier = models.ForeignKey(
        Courier, blank=True, null=True,
        on_delete=models.CASCADE)

    final_destination = models.ForeignKey(
        Department,
        null=True,
        blank=True,
        on_delete=models.CASCADE)

    receiver_at_destination = models.ForeignKey(
        User,
        null=True,
        blank=True,
        related_name='user',
        on_delete=models.CASCADE)

    status = models.CharField(
        verbose_name="Status",
        max_length=20,
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
