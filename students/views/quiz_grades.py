# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count

from ..models.quiz_grades import Grade

from ..util import make_order_by, django_paginator

def grades_list(request):
    # Set field name for ordering by default
    order_by_default = 'quiz_name__subject'
    # Set number of row per page
    row_per_page = 3

    query_set = Grade.objects.all()
    # Get list of all model's fields name
    fields = Grade._meta.get_all_field_names()
    # Set parameters for ordering
    order_by = request.GET.get('order_by', order_by_default)
    reverse = request.GET.get('reverse', '')
    # try to order group list
    query_set = make_order_by(fields, query_set, order_by, reverse)

    # paginator groups
    page = request.GET.get('page')
    query_set = django_paginator(query_set, page, row_per_page)

    return render(request, 'students/quiz_grades_list.html',
                  {'query_set': query_set,
                   'order_by_default': order_by_default})

def grades_short_list(request):
    """
    List of unique quizes and numbers of students that have particular quiz.
    """
    # TODO: add sort by quiz subject and date (as for students list)

    short = Grade.objects.values('quiz_name__subject',
                                 'quiz_name__date_time',
                                 'quiz_name_id').annotate(count_stud=
                                 Count('quiz_name')).order_by('quiz_name__subject')
    return render(request, 'students/quiz_grades_short_list.html',
                  {'short_list':short})

#   grades_quiz_detail_list
def quiz_grades_detail_list(request, qid):
    """
    Get list of students and their grades that relative to particular quiz.
    qid is the id of quez. The list is ordered by students last names.
     """

    # Set field name for ordering by default
    order_by_default = 'student_name__last_name'
    # Set number of row per page
    row_per_page = 3

    query_set = Grade.objects.filter(quiz_name_id=qid).order_by(order_by_default)
     # Get list of all model's fields name
    fields = Grade._meta.get_all_field_names()
    # Set parameters for ordering
    order_by = request.GET.get('order_by', order_by_default)
    reverse = request.GET.get('reverse', '')
    # try to order list
    query_set = make_order_by(fields, query_set, order_by, reverse)

    # paginator for list
    page = request.GET.get('page')
    query_set = django_paginator(query_set, page, row_per_page)

    return render(request, 'students/quiz_grades_detail_list.html',
                  {'query_set': query_set,
                   'order_by_default': order_by_default})

def grades_student_detail_list(request, sid):
    """
    Get list of quizes and grades that relative to particular student
    sid is the id of student. The list is ordered by quiz names.
     """
    # Set field name for ordering by default
    order_by_default = 'quiz_name__subject'
    # Set number of row per page
    row_per_page = 3

    query_set = Grade.objects.filter(student_name_id=sid).order_by(order_by_default)
     # Get list of all model's fields name
    fields = Grade._meta.get_all_field_names()
    # Set parameters for ordering
    order_by = request.GET.get('order_by', order_by_default)
    reverse = request.GET.get('reverse', '')
    # try to order list
    query_set = make_order_by(fields, query_set, order_by, reverse)

    # paginator for list
    page = request.GET.get('page')
    query_set = django_paginator(query_set, page, row_per_page)

    return render(request, 'students/grades_student_detail_list.html',
                  {'query_set': query_set,
                   'order_by_default': order_by_default})

def grades_add(request):
    return HttpResponse('<h1>Grade Add Form</h1>')

def grades_edit(request, grid):
    return HttpResponse('<h1>Edit Grade %s</h1>' % grid)

def grades_delete(request, grid):
    return HttpResponse('<h1>Delete Greade %s</h1>' % grid)
