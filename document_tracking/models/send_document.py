from datetime import date
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_search.model_mixins import SearchSlugModelMixin
from bhp_personnel.models import Department, Employee
from .document import Document
from .proxy_user import ProxyUser
from ..choices import DOCUMENT_STATUS, PRIORITY


class SendDocument(BaseUuidModel, SearchSlugModelMixin,
                   SiteModelMixin, models.Model):

    doc_identifier = models.CharField(
        verbose_name="Document Identifier",
        max_length=36,
        null=True,
        blank=True)

    document_name = models.CharField(
        verbose_name="Document Name",
        max_length=150,
        blank=False,
        null=True)

    department = models.ManyToManyField(
        Department,
        blank=True)

    send_to = models.ManyToManyField(
        ProxyUser,
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

    sent_date = models.DateField(
        verbose_name='Sent date',
        default=date.today,
        blank=True,
        null=True)

    group = models.ManyToManyField(
        Group,
        verbose_name='Group of people that can view this document',
        blank=True)

    received_by = models.CharField(
        verbose_name='Received By',
        max_length=100,
        blank=True,
        null=True)

    def get_dept(self):
        dept_list = ''
        for dept in self.department.all():
            dept_list = dept_list + dept.dept_name + ','
        return dept_list[:-1]

    def get_sent_to(self):
        sent_to_list = ''
        for sent_to in self.send_to.all():
            sent_to_list = sent_to_list + sent_to.username + ','
        return sent_to_list[:-1]

    def get_groups(self):
        group_list = ''
        for group in self.group.all():
            group_list = group_list + group.name + ','
        return group_list[:-1]

    def get_search_slug_fields(self):
        fields = super().get_search_slug_fields()
        fields.append('document_name')
        fields.append
        return fields

    def save(self, *args, **kwargs):
        try:
            doc_obj = Document.objects.get(doc_identifier=self.doc_identifier)
        except Document.DoesNotExist:
            raise
        else:
            self.document_name = doc_obj.document_name

        super().save(*args, **kwargs)
