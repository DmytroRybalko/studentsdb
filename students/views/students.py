# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for Students

def students_list(request):
    students = (
        {'id':1,
         'first_name': u'Дмитро',
         'last_name': u'Рибалко',
         'ticket': 235,
         'image': 'img/my_bike.jpg'},
        {'id': 2,
            'first_name': u'Вікторія',
            'last_name': u'Якуніна',
            'ticket': 2123,
            'image': 'img/vika.jpg'},
        {'id': 3,
            'first_name': u'Корост',
            'last_name': u'Андрій',
            'ticket': 2125,
            'image': 'img/GoITnewLife.jpg'}
    )
    return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
    return HttpResponse('<h1>Students Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)