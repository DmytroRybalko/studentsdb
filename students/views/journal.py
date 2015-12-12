# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

def students_log(request):
    return render(request, 'students/student_log.html', {})