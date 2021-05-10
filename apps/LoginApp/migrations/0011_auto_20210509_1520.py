# Generated by Django 3.1.5 on 2021-05-09 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginApp', '0010_auto_20210509_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='kvantuser',
            name='color',
            field=models.CharField(choices=[('Оранжевый', 'orange'), ('Синий', 'blue')], default='blue', max_length=100),
        ),
        migrations.AddField(
            model_name='kvantuser',
            name='theme',
            field=models.CharField(choices=[('Темная', 'dark'), ('Светлая', 'light')], default='light', max_length=100),
        ),
    ]
