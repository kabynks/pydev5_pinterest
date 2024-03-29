# Generated by Django 4.2 on 2024-02-17 15:44

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profilemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=1, editable=False, populate_from='username', unique=True),
            preserve_default=False,
        ),
    ]
