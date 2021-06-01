from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):

    site_title = 'Document Tracking'
    site_header = 'Document Tracking'
    index_title = 'Document Tracking'
    site_url = '/administration/'
    enable_nav_sidebar = False


document_tracking_admin = AdminSite(name='document_tracking_admin')
