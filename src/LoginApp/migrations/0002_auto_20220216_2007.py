# Generated by Django 3.1.5 on 2022-02-16 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LoginApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kvantuser',
            options={},
        ),
        migrations.AlterModelTable(
            name='kvantuser',
            table='kvant_user',
        ),
    ]