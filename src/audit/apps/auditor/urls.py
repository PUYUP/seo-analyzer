from django.urls import path

from .views import AnalyzingAjaxView, GetLatestNews

urlpatterns = [
    path('analyzing/', AnalyzingAjaxView.as_view(), name='analyzing_ajax'),
    path('getnews/', GetLatestNews.as_view(), name='getnews_ajax')
]

app_name = 'auditor'
