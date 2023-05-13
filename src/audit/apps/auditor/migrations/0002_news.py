# Generated by Django 4.2.1 on 2023-05-13 17:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('auditor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('content', models.TextField()),
                ('author_name', models.CharField(blank=True, max_length=255, null=True)),
                ('published_at', models.CharField(max_length=255)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
