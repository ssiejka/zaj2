# -*- coding: utf-8 -*-


def xrange(start_stop, stop=None, step=None):
    """
    Funkcja która działa jak funkcja range (wbudowana i z poprzednich zajęć)
    która działa dla liczb całkowitych.
    """
    table=[]
    if stop is None:
        stop=start_stop
        start=0
    else:
        start=start_stop
    if step is None:
        step=1
    n=start
    #yield n
    #table.append(n)
    while n < stop:
        yield n
        n=n+step
        #table.append(n)
    #return table

