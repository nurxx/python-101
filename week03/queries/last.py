from filter import *

def last(filename,**kwargs):
    result = filter(filename,**kwargs)
    return result[-1]