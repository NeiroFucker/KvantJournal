# Generated by Django 3.1.5 on 2022-08-16 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kvantcoursetype',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]