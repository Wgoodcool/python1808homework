# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-14 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=22, verbose_name='名字')),
                ('profrssion', models.CharField(max_length=22, verbose_name='职业')),
                ('power', models.IntegerField(db_column='hero_power', default=8000, verbose_name='战斗力')),
                ('birth_date', models.DateField(auto_now=True, verbose_name='出生日期')),
                ('last_date', models.DateField(auto_now=True, verbose_name='消失日期')),
                ('is_used', models.BooleanField(default=True, verbose_name='是否飞升')),
            ],
            options={
                'verbose_name': '英雄类',
                'db_table': '飞升战力表',
            },
        ),
    ]