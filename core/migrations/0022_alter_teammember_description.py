# Generated by Django 5.1.6 on 2025-02-13 09:42

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_services_is_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='description',
            field=tinymce.models.HTMLField(verbose_name='description'),
        ),
    ]
