# Generated by Django 3.1.5 on 2021-11-09 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DiaryApp', '0004_auto_20211109_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kvanthometask',
            name='task',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='kvanthomework',
            name='text',
            field=models.TextField(),
        ),
    ]
