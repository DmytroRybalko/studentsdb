# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.views.generic import UpdateView, DeleteView
from django.forms import ModelForm
#
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit
# from crispy_forms.bootstrap import FormActions
#
from ..models.students import Student
from ..models.groups import Group
from ..models.quiz import Quiz

# Views for Quizes

def quiz_list(request):
    # Set field name for ordering by default
    order_by_default = 'subject'
    quiz = Quiz.objects.all()

    # Collect sorted student's id into separate list
    quiz_pk =[pk.pk for pk in quiz]

    # Get list of all model's fields name
    quiz_fields = Quiz._meta.get_all_field_names()

    # try to order students list
    order_by = request.GET.get('order_by', order_by_default)
    if order_by in quiz_fields:
        quiz = quiz.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            quiz = quiz.reverse()
    #
    # paginator students
    paginator = Paginator(quiz, 3)
    page = request.GET.get('page')
    try:
        quiz = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an Integer, deliver first page.
        quiz = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver
        # last page of results.
        quiz = paginator.page(paginator.num_pages)

    return render(request, 'students/quiz_list.html',
                  {'quizes': quiz,
                   'quiz_pk': quiz_pk,
                   'order_by_default':order_by_default}
                  )

def quiz_add(request):
    return HttpResponse('<h1>Quiz Add Form</h1>')

def quiz_edit(request, qid):
    return HttpResponse('<h1>Edit Quiz %s</h1>' % qid)

def quiz_delete(request, qid):
    return HttpResponse('<h1>Delete Quiz %s</h1>' % qid)


