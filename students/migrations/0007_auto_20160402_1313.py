# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_quiz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='group',
        ),
        migrations.AddField(
            model_name='quiz',
            name='group_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u0413\u0440\u0443\u043f\u0430', blank=True, to='students.Group', null=True),
        ),
    ]
