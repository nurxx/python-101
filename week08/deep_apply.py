def deep_apply(func, data):
    if not callable(func):
        raise TypeError('First positional argument must be callable object!')

    for key, value in data.items():
        data[func(key)] = data.pop(key)

        if hasattr(value,'__iter__'):
            if isinstance(value,dict):
                deep_apply(func,value)
            else:
                for elem in value:
                    deep_apply(func, elem)

if __name__ == '__main__':
    def func(key):
        return str(key)

    data = {
            'a': 1,
            'b': {
                'c': 3,
                'd': [{(1,2): 5}],
                'f': {
                    'g': 6,
                    11:11
                }
            }
        }

    deep_apply(func,data)
    print(data)
