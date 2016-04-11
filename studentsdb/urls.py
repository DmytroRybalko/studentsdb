"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from .settings import MEDIA_ROOT, DEBUG
from students.views.students import StudentUpdateView, StudentDeleteView


urlpatterns = patterns('',
    # Students urls
    url(r'^$', 'students.views.students.students_list', name='home'),

    url(r'^students/add/$', 'students.views.students.students_add',
        name='students_add'),

    url(r'students/(?P<pk>\d+)/edit/$',
        StudentUpdateView.as_view(), name='students_edit'),

    url(r'students/(?P<pk>\d+)/delete/$',
        StudentDeleteView.as_view(), name='students_delete'),

    # Group urls
    url(r'^groups/$', 'students.views.groups.groups_list', name='groups'),

    url(r'^groups/add/$', 'students.views.groups.groups_add', name='groups_add'),

    url(r'^groups/(?P<gid>\d+)/edit/$', 'students.views.groups.groups_edit',
        name='groups_edit'),

    url(r'^groups/(?P<gid>\d+)/delete/$', 'students.views.groups.groups_delete',
        name='groups_delete'),

     # Quizes grade urls
    url(r'^grades/$', 'students.views.quiz_grades.grades_list', name='grades'),

    url(r'^grades/short/$', 'students.views.quiz_grades.grades_short_list', name='grades_short_list'),

    url(r'^grades/add/$', 'students.views.quiz_grades.grades_add', name='grades_add'),

    url(r'^grades/(?P<grid>\d+)/edit/$', 'students.views.quiz_grades.grades_edit',
        name='grades_edit'),

    url(r'^grades/(?P<grid>\d+)/delete/$', 'students.views.quiz_grades.grades_delete',
        name='grades_delete'),

    url(r'^grades/(?P<qid>\d+)/quiz_detail_list/$', 'students.views.quiz_grades.quiz_grades_detail_list',
        name='quiz_detail_list'),

    url(r'^grades/(?P<sid>\d+)/grades_student_detail_list/$', 'students.views.quiz_grades.grades_student_detail_list',
        name='grades_student_detail_list'),

    # Journal urls
    url(r'^journal/$', 'students.views.journal.students_log', name='journal'),

    # Quiz urls
    url(r'^quiz/$', 'students.views.quiz.quiz_list', name='quiz'),

    url(r'^quiz/add/$', 'students.views.quiz.quiz_add', name='quiz_add'),

    url(r'^quiz/(?P<qid>\d+)/edit/$', 'students.views.quiz.quiz_edit',
        name='quiz_edit'),

    url(r'^quiz/(?P<qid>\d+)/delete/$', 'students.views.quiz.quiz_delete',
        name='quiz_delete'),

    url(r'^admin/', include(admin.site.urls)),

    # Contact Admin Form
    url(r'^contact-admin/$', 'students.views.contact_admin.contact_admin',
        name='contact_admin'),
    )


if DEBUG:
    # serve files from media folder
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': MEDIA_ROOT}))
