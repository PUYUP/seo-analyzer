from django.contrib import admin
from .models import Analyzer, AnalyzerLog

admin.site.register(Analyzer)
admin.site.register(AnalyzerLog)
