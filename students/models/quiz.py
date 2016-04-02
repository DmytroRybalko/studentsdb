# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Quiz(models.Model):
    """ Group Quiz """

    class Meta(object):
        verbose_name = u"Іспити"
        verbose_name_plural = u"Іспити"

    subject = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Предмет")

    date_time = models.DateTimeField(
        blank=False,
        verbose_name=u"Дата та час складання")

    professor = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Викладач") # Петренко В.В.

    group_name = models.ForeignKey('Group',
        blank=False,
        null=False,
        verbose_name=u"Група",
        on_delete=models.PROTECT)

    def __unicode__(self):
        return u"%s (%s)" % (self.subject, self.date_time.date())