# -*- coding: utf-8 -*-
"""
This module contains function for generation list of days with as numbers and
 week's days for particular month.
"""
import calendar

def calendar_of_month(year, month):
    day_num = []
    days = (u'Пн', u'Вт', u'Ср', u'Чт', u'Пт', u'Сб', u'Нд')
    weekdays = calendar.monthcalendar(year, month)
    for week in weekdays:
        for day, date in zip(days, week):
            if date:
                day_num.append({'day':day, 'date':date})
    return tuple(day_num)

if __name__ == "__main__":
    print "Test calendar_of_month function"
    days = (u'Пн', u'Вт', u'Ср', u'Чт', u'Пт', u'Сб', u'Нд')
    weekdays = calendar.monthcalendar(2015, 11)
    print "November, 2015: ", weekdays, '\n'
    a = calendar_of_month(2015,11)
    for date in a:
        print date['day'], date['date']
    print a