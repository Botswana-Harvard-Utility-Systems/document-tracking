from django.urls.conf import path
from django.contrib import admin
from django.views.generic.base import RedirectView

from .admin_site import document_tracking_admin

app_name = 'document_tracking'

urlpatterns = [
    path('administrator/', document_tracking_admin.urls),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='administrator/'), name='home_url')
]
