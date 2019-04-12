from contextlib import contextmanager

@contextmanager
def assertRaises(some_exception,message=None):
    try:
        yield
        raise Exception('Exception not found!')
    except Exception as exc:
        if not isinstance(some_exception,tuple):
            if type(exc) == some_exception:
                if message is not None and message == str(exc):
                    return True
                elif message != str(exc) and message is not None:
                    raise Exception('Message is wrong')

            raise Exception('Exception found,but it\'s not {0}'.format(some_exception))

# def sum(a,b):
#     if type(a) is str or type(b) is str:
#         raise TypeError('Str type not allowed!')

#     return True

# with assertRaises(TypeError,'Str type not allowed!'):
#     print(sum('1',2)) #-> Exception raised, returned True

# with assertRaises(TypeError,'Sum of str and int not allowed!'):
#     print(sum('1',2)) #-> Message is wrong

# with assertRaises(TypeError):
#     print(sum(1,2)) # -> Raised 'Exception not found!'

