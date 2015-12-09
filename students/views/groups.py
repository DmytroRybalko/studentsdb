# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


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