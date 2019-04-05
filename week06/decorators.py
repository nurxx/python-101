import datetime
from time import sleep,time
from functools import wraps

start_time = time()

def accepts(*accept_args):
    def accepter(func):
        def decorated(*func_args):
            for index,item in enumerate(func_args):
                if type(item) != accept_args[index]:
                    raise TypeError('Argument {0} of {1} is not {2}!'.format(index+1,func.__name__,accept_args[index]))
            return func(*func_args)
        return decorated
    return accepter

def encrypt(integer):
    def wrapper(func):
        @wraps(func)
        def decorate(*args,**kwargs):
            encrypted = ""
            if len(args) == 0 and len(kwargs) == 0:
                for index,char in enumerate(func()):
                    if char.isalpha():
                        encrypted += chr(ord(char)+integer)
                    else:
                        encrypted += char
            return encrypted
        return decorate
    return wrapper


def log(filename):
    def wrapper(func):
        with open(filename,'a') as f:
            f.write('{0} was called at {1}\n'.format(func.__name__,datetime.datetime.now()))
        return func
    return wrapper

def performance(filename):
    def wrapper(func):
        with open(filename,'a') as f:
            f.write('{0} was called and took {1} seconds to execute\n'.format(func.__name__,'%.2f'%(time()-start_time)))
        return func
    return wrapper





