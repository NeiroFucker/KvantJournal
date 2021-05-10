# Generated by Django 3.1.5 on 2021-05-09 04:26

import LoginApp.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SystemModule', '0001_initial'),
        ('LoginApp', '0008_remove_kvantuser_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='kvantuser',
            name='image',
            field=models.ForeignKey(default=LoginApp.models.set_default_image, on_delete=django.db.models.deletion.CASCADE, to='SystemModule.imagestorage'),
        ),
    ]
