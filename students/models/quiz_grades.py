# -*- coding: utf-8 -*-

from django.db import models

class Grade(models.Model):
    """ Students Grades for Quiz """

    class Meta(object):
        verbose_name = u"Оцінка"
        verbose_name_plural = u"Оцінки"

    grade = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Оцінка")

    student_name = models.ForeignKey("Student",
        blank=False,
        null=False,
        verbose_name=u"Студент")

    quiz_name = models.ForeignKey('Quiz',
        blank=False,
        null=False,
        verbose_name=u"Іспит")

    def __unicode__(self):
        return u"%s, %s, %s" % (self.quiz_name.subject, self.student_name, self.grade)