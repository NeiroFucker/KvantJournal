# Generated by Django 3.1.5 on 2021-05-09 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SystemModule', '0001_initial'),
        ('LoginApp', '0005_auto_20210509_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kvantuser',
            name='image',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='SystemModule.imagestorage'),
        ),
    ]
