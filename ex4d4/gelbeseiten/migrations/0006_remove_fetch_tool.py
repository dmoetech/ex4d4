# Generated by Django 2.2.5 on 2020-02-05 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gelbeseiten', '0005_remove_scrapefile_tool'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fetch',
            name='tool',
        ),
    ]