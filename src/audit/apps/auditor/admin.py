from django.contrib import admin
from .models import Analyzer, AnalyzerLog, News

admin.site.register(Analyzer)
admin.site.register(AnalyzerLog)
admin.site.register(News)
