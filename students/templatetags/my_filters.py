# -*- coding: utf-8 -*-

from django import template

register = template.Library()


def get_order_number(seq, value):
    return seq.index(value) + 1

register.filter('order_number', get_order_number)