# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.views.generic import UpdateView, DeleteView
from django.forms import ModelForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

from ..models.students import Student
from ..models.groups import Group

class StudentUpdateForm(ModelForm):
    class Meta:
        model = Student
        exclude = ['notes']

    def __init__(self, *args, **kwargs):
        super(StudentUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        # set form tag attributes
        self.helper.form_action = reverse('students_edit',
                                          kwargs={'pk': kwargs['instance'].id})
        self.helper.form_method = "POST"
        self.helper.form_class = "form-horizontal"

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # add buttons
        self.helper.layout.append(FormActions(
            Submit('add_button', u'Зберегти', css_class="btn btn-primary"),
            Submit('cancel_button', u'Скасувати', css_class="btn btn-link"),
        ))

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
def students_edit(request, pk):
    student = Student.objects.filter(id=pk)[0]
    if request.method == "POST":
        if request.POST.get('edit_button') is not None:
            # error collection
            errors = {}
            # validate user input
            first_name = request.POST.get('first_name',
                                          student.first_name).strip()
            if not first_name:
                errors['first_name'] = u"Ім'я є обов'язковим"
            else:
                student.first_name = first_name

            last_name = request.POST.get('last_name',
                                         student.last_name).strip()
            if not last_name:
                errors['last_name'] = u"Прізвище є обов'язковим"
            else:
                student.last_name = last_name

            student.middle_name = request.POST.get('middle_name',
                                                   student.middle_name).strip()

            birthday = request.POST.get('birthday',
                                        student.birthday).strip()
            if not birthday:
                errors['birthday'] = u"Дата народження є обов'язковою"
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors['birthday'] = u"Введіть коректний формат дати (напр. 1981-02-30)"
                else:
                    student.birthday = birthday

            photo = request.FILES.get('photo')
            if photo:
                student.photo = photo

            ticket = request.POST.get('ticket', student.ticket).strip()
            if not ticket:
                errors['ticket'] = u"Номер білета є обов'язковим"
            else:
                student.ticket = ticket

            student_group = request.POST.get('student_group',
                                             student.student_group).strip()
            if not student_group:
                errors['student_group'] = u"Оберіть групу для студента"
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    errors['student_group'] = u"Оберіть корректну групу"
                else:
                    student.student_group = groups[0]

            student.notes = request.POST.get('notes', student.notes).strip()

            if not errors:
                student.save()
                messages.success(request, u'Студента %s успішно збережено!' %
                                 student)
                return redirect('home')

            else:
                # render from with errors and previous user input
                messages.error(request, u'Будь-ласка, виправте наступні помилки:')
                return render(request, 'students/students_edit.html',
                    {'student': student,
                     'groups': Group.objects.exclude(pk=student.student_group.id),
                     'errors': errors})

        elif request.POST.get('cancel_button') is not None:
            # redirect to home page on cancel button
            messages.warning(request,
                             u'Редагування студента %(name)s скасовано!' %
                             dict(name=student))
            return HttpResponseRedirect(reverse('home'))

    else:
        # initial form render
        return render(request, 'students/students_edit.html',
                    {'student': student,
                     'groups': Group.objects.exclude(pk=student.student_group.id)})

    # redirect to home page
    return render(request, 'students/students_edit.html',
                  {'student': student,
                   'groups': Group.objects.exclude(pk=student.student_group.id)})

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
        # was form add button clicked?
        if request.POST.get('add_button') is not None:
            # error collection
            errors = {}
            # validate student data will go here
            data = {'middle_name': request.POST.get('middle_name'),
                    'notes': request.POST.get('notes')}

            # validate user input
            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = u"Ім'я є обов'язковим"
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = u"Прізвище є обов'язковим"
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday', '').strip()
            if not birthday:
                errors['birthday'] = u"Дата народження є обов'язковою"
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors['birthday'] = u"Введіть коректний формат дати (напр. 1981-02-30)"
                else:
                    data['birthday'] = birthday

            ticket = request.POST.get('ticket', '').strip()
            if not ticket:
                errors['ticket'] = u"Номер білета є обов'язковим"
            else:
                data['ticket'] = ticket

            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = u"Оберіть групу для студента"
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    errors['student_group'] = u"Оберіть корректну групу"
                else:
                    data['student_group'] = groups[0]

            photo = request.FILES.get('photo')
            if photo:
                data['photo'] = photo

            # save student
            if not errors:
                student = Student(**data)
                student.save()
                messages.success(request, u'Студента %s успішно додано!' % student)
                # redirect user to students list
                # return HttpResponseRedirect(reverse('home'))
                return redirect('home')

            else:
                # render from with errors and previous user input
                messages.error(request, u'Будь-ласка, виправте наступні помилки:')
                return render(request, 'students/students_add.html',
                    {'groups': Group.objects.all().order_by('title'),
                     'errors': errors})

        elif request.POST.get('cancel_button') is not None:
            # redirect to home page on cancel button
            messages.warning(request, u'Додавання студента скасовано!')
            return HttpResponseRedirect(reverse('home'))

    else:
        # initial form render
        return render(request, 'students/students_add.html',
                    {'groups': Group.objects.all().order_by('title')})

    return render(request, 'students/students_add.html',
        {'groups': Group.objects.all().order_by('title')})
