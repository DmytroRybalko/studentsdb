# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_auto_20160402_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.CharField(max_length=256, verbose_name='\u041e\u0446\u0456\u043d\u043a\u0430')),
                ('quiz_name', models.ForeignKey(verbose_name='\u0406\u0441\u043f\u0438\u0442', to='students.Quiz')),
                ('student_name', models.OneToOneField(verbose_name='\u0421\u0442\u0443\u0434\u0435\u043d\u0442', to='students.Student')),
            ],
            options={
                'verbose_name': '\u041e\u0446\u0456\u043d\u043a\u0430',
                'verbose_name_plural': '\u041e\u0446\u0456\u043d\u043a\u0438',
            },
        ),
    ]
