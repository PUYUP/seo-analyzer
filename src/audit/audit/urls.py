from django.contrib import admin
from django.urls import path, include

from core import urls as core_urls
from apps.auditor import urls as auditor_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auditor/', include((auditor_urls, 'auditor'),
         namespace='auditor'), name='auditor'),
    path('', include((core_urls, 'core'), namespace='core'), name='core'),
]
