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

    action_date = models.DateField(
        verbose_name='Action date',
        default=date.today,
        blank=True,
        null=True,
    )

    group = models.ManyToManyField(
        Group,
        verbose_name='Group of people that can view this document',)

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

    def get_final_dest(self):
        final_dest_list = ''
        for final_dest in self.final_destination.all():
            final_dest_list = final_dest_list + final_dest.dept_name + ','
        return final_dest_list[:-1]

    def get_final_dest_rec(self):
        final_dest_rec_list = ''
        for final_dest_rec in self.receiver_at_destination.all():
            final_dest_rec_list = final_dest_rec_list + final_dest_rec.username + ','
        return final_dest_rec_list[:-1]

    def save(self, *args, **kwargs):
        super(SendDocument, self).save(*args, **kwargs)

    class Meta:
        unique_together = ['doc_identifier',]
