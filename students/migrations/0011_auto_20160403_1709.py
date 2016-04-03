# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='student_name',
            field=models.ForeignKey(verbose_name='\u0421\u0442\u0443\u0434\u0435\u043d\u0442', to='students.Student'),
        ),
    ]
