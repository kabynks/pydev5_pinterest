# Generated by Django 4.2 on 2024-02-05 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0012_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
