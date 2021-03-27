# Generated by Django 3.1.5 on 2021-03-26 12:21

import GeneralPage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentPage', '0002_delete_kvantmessage'),
        ('GeneralPage', '0002_auto_20210326_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kvantnews',
            name='image',
            field=models.ForeignKey(blank=True, default=GeneralPage.models.setDefaultImage, on_delete=models.SET(GeneralPage.models.setDefaultImage), to='StudentPage.imagestorage'),
        ),
    ]
