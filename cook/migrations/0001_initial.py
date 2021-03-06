# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-15 09:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0006_auto_20180815_0913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('information', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_open', models.BooleanField(default=True)),
                ('businessunit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='account.BusinessUnit')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='account.Position')),
            ],
        ),
    ]
