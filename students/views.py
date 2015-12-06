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

# Vies for Groups
groups = (
        {'id':1,
            'group_name': u'ВЛ-81',
            'steward': u'Баличева Анна'},
        {'id': 2,
            'group_name': u'ВА-81',
            'steward': u'Якуніна Вікторія'},
        {'id': 3,
            'group_name': u'ВТ-81',
            'steward': u'Корост Андрій'}
    )

def groups_list(request):
    return render(request, 'students/group_list.html', {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)

