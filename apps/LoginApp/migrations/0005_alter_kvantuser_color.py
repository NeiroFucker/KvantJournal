# Generated by Django 3.2.3 on 2021-09-06 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginApp', '0004_auto_20210901_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kvantuser',
            name='color',
            field=models.CharField(choices=[('green', 'green'), ('blue', 'blue'), ('red', 'red')], default='blue', max_length=100),
        ),
    ]