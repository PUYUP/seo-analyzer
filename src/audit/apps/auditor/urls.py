from django.urls import path

from .views import AnalyzingAjaxView

urlpatterns = [
    path('analyzing/', AnalyzingAjaxView.as_view(), name='analyzing_ajax')
]

app_name = 'auditor'
