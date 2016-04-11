# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count

# from ..models.students import Student
# from ..models.groups import Group
from ..models.quiz_grades import Grade

def grades_list(request):
    # Set field name for ordering by default
    order_by_default = 'quiz_name'
    grades = Grade.objects.all()

    # Collect sorted group's id into separate list
    grades_pk =[pk.pk for pk in grades]

    # Get list of all model's fields name
    fields = Grade._meta.get_all_field_names()

    # try to order students list
    order_by = request.GET.get('order_by', order_by_default)
    if order_by in fields:
        grades = grades.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            grades = grades.reverse()

    # paginator grades
    paginator = Paginator(grades, 3)
    page = request.GET.get('page')
    try:
        grades = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an Integer, deliver first page.
        grades = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver
        # last page of results.
        grades = paginator.page(paginator.num_pages)

    return render(request, 'students/quiz_grades_list.html',
                  {'grades': grades,
                   'grades_pk': grades_pk,
                   'order_by_default':order_by_default})

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
    details = Grade.objects.filter(quiz_name_id=qid).order_by('student_name__last_name')
    return render(request, 'students/quiz_grades_detail_list.html',
                  {'details':details})

def grades_student_detail_list(request, sid):
    """
    Get list of quizes and grades that relative to particular student
    sid is the id of student. The list is ordered by quiz names.
     """
    details = Grade.objects.filter(student_name_id=sid).order_by('quiz_name__subject')
    return render(request, 'students/grades_student_detail_list.html',
                  {'details': details})

def grades_add(request):
    return HttpResponse('<h1>Grade Add Form</h1>')

def grades_edit(request, grid):
    return HttpResponse('<h1>Edit Grade %s</h1>' % grid)

def grades_delete(request, grid):
    return HttpResponse('<h1>Delete Greade %s</h1>' % grid)
