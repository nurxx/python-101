from filter import *

def count(filename,**kwargs):
    result = filter(filename,**kwargs)
    return len(result)