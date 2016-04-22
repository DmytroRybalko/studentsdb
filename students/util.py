# -*- coding: utf-8 -*-

def make_order_by(model_fields, query_set, order_by, reverse):

    if order_by or order_by.split('__')[0] in model_fields:
        query_set = query_set.order_by(order_by)
        if reverse == '1':
            query_set = query_set.reverse()
    return query_set