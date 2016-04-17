# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models.students import Student
from ..models.groups import Group

def groups_list(request):
    # Set field name for ordering by default
    order_by_default = 'title'
    groups = Group.objects.all()

    # Collect sorted group's id into separate list
    groups_pk =[pk.pk for pk in groups]

    # Get list of all model's fields name
    fields = Group._meta.get_all_field_names()

    # try to order students list
    order_by = request.GET.get('order_by', order_by_default)
    # second condition let us sort by field in related model
    if order_by or order_by.split('__')[0] in fields:
        groups = groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            groups = groups.reverse()

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
                   'groups_pk': groups_pk,
                   'order_by_default':order_by_default})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)