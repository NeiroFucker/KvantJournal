# Generated by Django 3.1.5 on 2021-05-09 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SystemModule', '0001_initial'),
        ('LoginApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kvantuser',
            name='image',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='SystemModule.imagestorage'),
        ),
    ]
