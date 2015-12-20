# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from calendar_generator import calendar_of_month
from students import students_list

def students_log(request):
    calendar = calendar_of_month(2015,11)
    #calendar = ({'date': 1, 'day': u'Пн'}, {'date': 2, 'day':u'Вт'}, ...)
    students = (
        {'id': 1,
         'name': u'Дмитро\nРибалко'},
        {'id': 2,
         'name': u'Вікторія\nЯкуніна'},
        {'id': 3,
         'name': u'Віктор\nКоцюба'}
    )
    return render(request, 'students/student_log.html', {'calendar':calendar,
                                                         'students':students})
