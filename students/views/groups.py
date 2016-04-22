# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models.students import Student
from ..models.groups import Group

from ..util import make_order_by, django_paginator

def groups_list(request):
    # Set field name for ordering by default
    order_by_default = 'title'
    query_set = Group.objects.all()
     # Get list of all model's fields name
    fields = Group._meta.get_all_field_names()
    order_by = request.GET.get('order_by', order_by_default)
    reverse = request.GET.get('reverse', '')
    # try to order group list
    query_set = make_order_by(fields, query_set, order_by, reverse)

    # paginator groups
    row_per_page = 3
    page = request.GET.get('page')
    query_set = django_paginator(query_set, page, row_per_page)

    return render(request, 'students/group_list.html',
                  {'order_by_default': order_by_default,
                   'query_set': query_set,
                   'order_by': order_by,
                   'reverse': reverse})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)