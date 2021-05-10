# Generated by Django 3.1.5 on 2021-05-07 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AdminModule', '0001_initial'),
        ('LoginApp', '0001_initial'),
        ('DiaryApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kvantlesson',
            name='mark',
            field=models.ManyToManyField(blank=True, to='DiaryApp.KvantLessonMark'),
        ),
        migrations.AddField(
            model_name='kvantlesson',
            name='task',
            field=models.ManyToManyField(blank=True, to='DiaryApp.KvantLessonHomeWork'),
        ),
        migrations.AddField(
            model_name='kvantcourse',
            name='students',
            field=models.ManyToManyField(blank=True, to='LoginApp.KvantStudent'),
        ),
        migrations.AddField(
            model_name='kvantcourse',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LoginApp.kvantteacher'),
        ),
    ]