from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):

    name = 'document_tracking'
    verbose_name = 'Document Tracking'
    admin_site_name = 'document_tracking_admin'
    identifier_pattern = None
