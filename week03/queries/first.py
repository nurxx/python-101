from filter import *

def first(filename,**kwargs):
    result = filter(filename,**kwargs)
    return result[0]