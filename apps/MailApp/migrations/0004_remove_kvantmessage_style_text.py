# Generated by Django 3.1.5 on 2021-11-09 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MailApp', '0003_auto_20210613_1322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kvantmessage',
            name='style_text',
        ),
    ]
