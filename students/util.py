# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def make_order_by(model_fields, query_set, order_by, reverse):

    if order_by or order_by.split('__')[0] in model_fields:
        query_set = query_set.order_by(order_by)
        if reverse == '1':
            query_set = query_set.reverse()
    return query_set

def django_paginator(query_set, page, row_per_page):
    paginator = Paginator(query_set, row_per_page)
    try:
        query_set = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an Integer, deliver first page.
        query_set = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver
        # last page of results.
        query_set = paginator.page(paginator.num_pages)
    return query_set