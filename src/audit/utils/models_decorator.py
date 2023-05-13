import uuid

from django.db import models


def with_timestamp_and_uuid(cls: models.Model):
    # create fields for creation and modification times
    models.UUIDField(default=uuid.uuid4, editable=False, db_index=True) \
        .contribute_to_class(cls, name='uuid')
    models.DateTimeField(auto_now_add=True) \
        .contribute_to_class(cls, name='created_at')
    models.DateTimeField(auto_now=True) \
        .contribute_to_class(cls, name='updated_at')

    return cls
