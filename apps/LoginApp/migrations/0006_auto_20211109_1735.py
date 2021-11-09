# Generated by Django 3.1.5 on 2021-11-09 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginApp', '0005_alter_kvantuser_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kvantuser',
            name='color',
            field=models.CharField(choices=[('green', 'green'), ('blue', 'blue'), ('red', 'red')], default='blue', max_length=10),
        ),
        migrations.AlterField(
            model_name='kvantuser',
            name='permission',
            field=models.CharField(choices=[('Ученик', 'Ученик'), ('Учитель', 'Учитель'), ('Администратор', 'Администратор')], max_length=20),
        ),
        migrations.AlterField(
            model_name='kvantuser',
            name='theme',
            field=models.CharField(choices=[('dark', 'dark'), ('light', 'light')], default='light', max_length=10),
        ),
    ]
