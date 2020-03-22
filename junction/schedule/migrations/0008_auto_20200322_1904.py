# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-03-22 13:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0007_auto_20160623_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduleitem',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_scheduleitem_set', to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AlterField(
            model_name='scheduleitem',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_scheduleitem_set', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AlterField(
            model_name='scheduleitem',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='conferences.Room'),
        ),
        migrations.AlterField(
            model_name='scheduleitem',
            name='session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='proposals.Proposal'),
        ),
        migrations.AlterField(
            model_name='scheduleitemtype',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_scheduleitemtype_set', to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AlterField(
            model_name='scheduleitemtype',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_scheduleitemtype_set', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
    ]
