# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from ..models.quiz import Quiz

from ..util import make_order_by, django_paginator

# Views for Quizes

def quiz_list(request):
    # Set field name for ordering by default
    order_by_default = 'subject'
    # Set number of row per page
    row_per_page = 3

    query_set = Quiz.objects.all()
     # Get list of all model's fields name
    fields = Quiz._meta.get_all_field_names()
     # Set parameters for ordering
    order_by = request.GET.get('order_by', order_by_default)
    reverse = request.GET.get('reverse', '')
    # try to order group list
    query_set = make_order_by(fields, query_set, order_by, reverse)

    # paginator groups
    page = request.GET.get('page')
    query_set = django_paginator(query_set, page, row_per_page)

    return render(request, 'students/quiz_list.html',
                  {'query_set': query_set,
                   'order_by_default': order_by_default})

def quiz_add(request):
    return HttpResponse('<h1>Quiz Add Form</h1>')

def quiz_edit(request, qid):
    return HttpResponse('<h1>Edit Quiz %s</h1>' % qid)

def quiz_delete(request, qid):
    return HttpResponse('<h1>Delete Quiz %s</h1>' % qid)


