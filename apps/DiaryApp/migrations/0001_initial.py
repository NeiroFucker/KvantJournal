# Generated by Django 3.1.5 on 2021-05-07 12:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SystemModule', '0001_initial'),
        ('LoginApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KvantLessonMark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('ОТ', 'ОТ'), ('УП', 'УП')], max_length=150)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='KvantLessonHomeWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField()),
                ('file', models.ManyToManyField(blank=True, to='SystemModule.FileStorage')),
                ('students', models.ManyToManyField(blank=True, to='LoginApp.KvantStudent')),
            ],
        ),
    ]