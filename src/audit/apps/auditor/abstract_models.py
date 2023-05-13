from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models_decorator import with_timestamp_and_uuid


@with_timestamp_and_uuid
class AbstractAnalyzer(models.Model):
    source = models.URLField(max_length=500, db_index=True)

    class Meta:
        abstract = True
        app_label = 'auditor'


@with_timestamp_and_uuid
class AbstractAnalyzerLog(models.Model):
    """
    Maybe one website has multiple times anaylzing,
    so we record as log

    :metadata:
        stored source information like title, content,
        links, etc

    Note! use JSONField for stored `metadata` is not best practice
    we can use eav method in the future
    """
    analyzer = models.ForeignKey('auditor.Analyzer',
                                 related_name='logs',
                                 on_delete=models.CASCADE)
    metadata = models.JSONField(help_text=_("Extracted data title, content"))

    class Meta:
        abstract = True
        app_label = 'auditor'
