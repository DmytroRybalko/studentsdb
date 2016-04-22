# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models.students import Student
from ..models.groups import Group

from ..util import make_order_by

def groups_list(request):
    # Set field name for ordering by default
    order_by_default = 'title'
    groups = Group.objects.all()
     # Get list of all model's fields name
    fields = Group._meta.get_all_field_names()
    order_by = request.GET.get('order_by', order_by_default)
    reverse = request.GET.get('reverse', '')
    # try to order groups list
    groups = make_order_by(fields, groups, order_by, reverse)

    # paginator groups
    paginator = Paginator(groups, 3)
    page = request.GET.get('page')
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an Integer, deliver first page.
        groups = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver
        # last page of results.
        groups = paginator.page(paginator.num_pages)

    return render(request, 'students/group_list.html',
                  {'groups': groups,
                   'order_by_default':order_by_default})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)