# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-05 00:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160603_0025'),
    ]

    operations = [
        migrations.CreateModel(
            name='addsubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectname', models.CharField(max_length=100)),
                ('subjectfile', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='addtheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('themename', models.CharField(max_length=100)),
                ('themefile', models.FileField(upload_to='')),
            ],
        ),
    ]
