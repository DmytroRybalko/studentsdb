# -*- coding: utf-8 -*-

from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.forms import ModelForm

from crispy_forms.bootstrap import FormActions, PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from ..models.students import Student
from ..models.groups import Group

class StudentActionForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'middle_name', 'birthday',
                  'photo', 'ticket', 'student_group', 'notes']

    def __init__(self, *args, **kwargs):

        super(StudentActionForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        # set form tag attributes
        try:
            self.helper.form_action = reverse('students_edit',
                                          kwargs={'pk': kwargs['instance'].id})
        except KeyError:
            self.helper.form_action = reverse('students_add')

        self.helper.form_method = "POST"
        self.helper.form_class = "form-horizontal"

        # set form field properties
        self.helper.help_text_inline = True
        # set False value to enable discard the changes while filling the form
        self.helper.html5_required = False
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # prepended text for setting placeholder
        self.helper.layout[3] = PrependedText(
            self.Meta.fields[3], '', placeholder="1981-01-01")

        # add buttons
        self.helper.layout.append(FormActions(
            Submit('add_button', u'Зберегти', css_class="btn btn-primary"),
            Submit('cancel_button', u'Скасувати', css_class="btn btn-link"),
        ))

################## Don't delete these forms ###########################

# class StudentUpdateForm(ModelForm):
#     class Meta:
#         model = Student
#         exclude = ['notes']
#
#     def __init__(self, *args, **kwargs):
#         super(StudentUpdateForm, self).__init__(*args, **kwargs)
#
#         self.helper = FormHelper(self)
#
#         # set form tag attributes
#         self.helper.form_action = reverse('students_edit',
#                                           kwargs={'pk': kwargs['instance'].id})
#         self.helper.form_method = "POST"
#         self.helper.form_class = "form-horizontal"
#
#         # set form field properties
#         self.helper.help_text_inline = True
#         self.helper.html5_required = True
#         self.helper.label_class = 'col-sm-2 control-label'
#         self.helper.field_class = 'col-sm-10'
#
#         # add buttons
#         self.helper.layout.append(FormActions(
#             Submit('add_button', u'Зберегти', css_class="btn btn-primary"),
#             Submit('cancel_button', u'Скасувати', css_class="btn btn-link"),
#         ))

# class StudentAddForm(ModelForm):
#     class Meta:
#         model = Student
#         fields = ['first_name', 'last_name', 'middle_name', 'birthday',
#                   'photo', 'ticket', 'student_group', 'notes']
#         # fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super(StudentAddForm, self).__init__(*args, **kwargs)
#
#         self.helper = FormHelper(self)
#
#         # set form tag attributes
#         self.helper.form_action = reverse('students_add')
#         self.helper.form_method = "POST"
#         self.helper.form_class = "form-horizontal"
#
#         # set form field properties
#         self.helper.help_text_inline = True
#         self.helper.html5_required = False
#         self.helper.label_class = 'col-sm-2 control-label'
#         self.helper.field_class = 'col-sm-10'
#
#         # prepended text for setting placeholder
#         self.helper.layout[3] = PrependedText(
#             self.Meta.fields[3], '', placeholder="1981-01-01")
#
#         # add buttons
#         self.helper.add_input(Submit('add_button', u'Додати',
#                                      css_class="btn btn-primary"))
#         self.helper.add_input(Submit('cancel_button', u'Скасувати',
#                                      css_class="btn btn-link"))
#         # alternative variant
#         # self.helper.layout.append(FormActions(
#         #     Submit('add_button', u'Зберегти', css_class="btn btn-primary"),
#         #     Submit('cancel_button', u'Скасувати', css_class="btn btn-link"),
#         # ))