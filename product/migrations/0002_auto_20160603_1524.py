# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='products',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photo'),
        ),
        migrations.AlterField(
            model_name='products',
            name='pname',
            field=models.CharField(default='', max_length=100),
        ),
    ]
