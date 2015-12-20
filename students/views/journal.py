# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from calendar_generator import calendar_of_month


def students_log(request):
    calendar = calendar_of_month(2015,11)
    #calendar = ({'date': 1, 'day': u'Пн'}, {'date': 2, 'day':u'Вт'}, ...)
    return render(request, 'students/student_log.html', {'calendar':calendar})
