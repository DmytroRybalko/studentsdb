# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_student_student_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='middle_name',
            field=models.CharField(max_length=256, null=True, verbose_name='\u041f\u043e-\u0431\u0430\u0442\u044c\u043a\u043e\u0432\u0456', blank=True),
        ),
    ]
