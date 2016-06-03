# -*- coding: utf-8 -*-

from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages

# from studentsdb.settings import ADMIN_EMAIL

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from contact_form.forms import ContactForm
from contact_form.views import ContactFormView

class AdminContactForm(ContactForm):

    subject_template_name = 'contact_admin/contact_form_subject.txt'
    template_name = 'contact_admin/contact_form.txt'

    def __init__(self, request=None, *args, **kwargs):
        # call original initializator
        super(AdminContactForm, self).__init__(request=request, *args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('contact_admin')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # form buttons
        self.helper.add_input(Submit('send_button', u'Надіслати'))


    def save(self, fail_silently=False):
        # send_mail(fail_silently=fail_silently, **self.get_message_dict())
        try:
            send_mail(fail_silently=fail_silently, **self.get_message_dict())
        except Exception:
            messages.error(self.request,
            u"Під час відправки листа виникла непередбачувана помилка."
            u"Спробуйте скористатися даною формою пізніше.")
        else:
            messages.success(self.request, u"Повідомлення успішно надіслане!")
        # messages.success(self.request, self.get_message_dict())

class AdminContactFormView(ContactFormView):
    form_class = AdminContactForm
    template_name = 'contact_admin/form.html'

    def get_success_url(self):
        return reverse('contact_admin')