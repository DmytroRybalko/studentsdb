# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20160327_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=256, verbose_name='\u041f\u0440\u0435\u0434\u043c\u0435\u0442')),
                ('date_time', models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u0442\u0430 \u0447\u0430\u0441 \u0441\u043a\u043b\u0430\u0434\u0430\u043d\u043d\u044f')),
                ('professor', models.CharField(max_length=256, verbose_name='\u0412\u0438\u043a\u043b\u0430\u0434\u0430\u0447')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='students.Group', null=True)),
            ],
            options={
                'verbose_name': '\u0406\u0441\u043f\u0438\u0442\u0438',
                'verbose_name_plural': '\u0406\u0441\u043f\u0438\u0442\u0438',
            },
        ),
    ]
