# Generated by Django 3.1.5 on 2022-04-16 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NotificationApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kvantnotification',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelTable(
            name='kvantnotification',
            table='kvant_notifications',
        ),
    ]
