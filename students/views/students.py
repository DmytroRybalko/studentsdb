# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import UpdateView, DeleteView, CreateView
from django.contrib import messages
from datetime import datetime

from ..forms.forms import StudentActionForm
from ..models.groups import Group
from ..models.students import Student


class StudentUpdateView(SuccessMessageMixin, UpdateView):
    model = Student
    template_name = 'students/students_edit.html'
    form_class = StudentActionForm
    success_message = u'Студента %(name)s успішно змінено!'

    def get_success_url(self):
        return reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.warning(request,
                           u'Редагування студента %(name)s скасовано!' %
                           dict(name=self.get_object()))
            return HttpResponseRedirect(reverse('home'))
        else:
            return super(StudentUpdateView, self).post(request, *args, **kwargs)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, name=self.get_object())

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/students_confirm_delete.html'
    success_message = u'Студента %(name)s успішно видалено!'

    def get_success_url(self):
        return reverse('home')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,
                         self.success_message % dict(name=self.get_object()))
        return super(StudentDeleteView, self).delete(request, *args, **kwargs)

# Views for Students
def students_list(request):
    # TODO: replace sort functionality to function
    # Set field name for ordering by default
    order_by_default = 'last_name'
    students = Student.objects.all()

    # Collect sorted student's id into separate list
    students_pk =[pk.pk for pk in students]

    # Get list of all model's fields name
    students_fields = Student._meta.get_all_field_names()

    # try to order students list
    order_by = request.GET.get('order_by', order_by_default)
    if order_by in students_fields:
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

     # paginator students
    row_per_page = 4
    rows_in_db = Student.objects.count()
    # calculate number of pages
    if rows_in_db % row_per_page:
        num_pages = (rows_in_db / row_per_page) + 1
    else:
        num_pages = (rows_in_db / row_per_page)
    try:
        page = int(request.GET.get('page'))
    except ValueError:
        # if page is empty string
        page = 1
    except TypeError:
        # if page is None
        page = 1
    paginator = students[row_per_page*(page-1):row_per_page*page]

    # order by order number ('№' field )
    order_num = row_per_page*page - (row_per_page - 1)
    # reverse ordering
    revorder_num = (num_pages - 1 - page)*row_per_page + rows_in_db % row_per_page
    if revorder_num < 0:
        revorder_num = 0

    return render(request, 'students/students_list.html',
                  {'students': paginator,
                   'order_num': order_num,
                   'revorder_num': revorder_num,
                   'page_range':range(1,num_pages + 1),
                   'page': page,
                   'order_by_default':order_by_default})

def students_add(request):
    # was form posted?
    if request.method == "POST":
        # create a form instance and populate it with data form the request
        form = StudentActionForm(request.POST)

        if request.POST.get('add_button') is not None:
            if form.is_valid():
                form.save()
                messages.success(request, u'Студента %s успішно додано!' % form.instance)
                return redirect('home')
        elif request.POST.get('cancel_button') is not None:
            messages.warning(request, u'Додавання студента скасовано!')
            return redirect('home')
    else:
        form = StudentActionForm()

    return render(request, 'students/students_add.html', {'form': form})
