# -*- coding: utf-8 -*-

from django import template

register = template.Library()


def get_order_number(seq, value):
    return seq.index(value) + 1

register.filter('order_number', get_order_number)

@register.simple_tag(takes_context=True)
def sort_field(context, **kwargs):
    """
    Function takes dictionary of arguments and return get request string
    that contains field for ordering and symbol arrow direction (up or down)
    accordinп to current context.

    List of arguments:
    url      -- the url short name for page
    order_by -- field of model for ordering
    name     -- field name for displaying
    """
    request = context['request']
    order_by_default = context['order_by_default']

    if not request.GET.items() and order_by_default == kwargs.get('order_by',''):
        link = "<a href=\"/%(url)s/?order_by=%(order_by)s&reverse=1\">" \
               "%(name)s &uarr;</a>" % dict(**kwargs)
    else:
        order_by = request.GET.get('order_by','NO_order_by')
        reverse = request.GET.get('reverse','NO_reverse')
        link = "<a href=\"/%(url)s/?order_by=%(order_by)s&reverse=\">" \
               "%(name)s</a>" % dict(**kwargs)
        if order_by == kwargs.get('order_by') and reverse != '1':
            link = "<a href=\"/%(url)s/?order_by=%(order_by)s&reverse=1\">" \
                   "%(name)s &uarr;</a>" % dict(**kwargs)
        elif order_by == kwargs.get('order_by') and reverse == '1':
            link = "<a href=\"/%(url)s/?order_by=%(order_by)s&reverse=\">" \
                   "%(name)s &darr;</a>" % dict(**kwargs)
    return link