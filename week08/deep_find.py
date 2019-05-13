def deep_find_dfs(data, key):
    for k, val in data.items():
        if k == key:
            return val

        if isinstance(val, dict):
            result = deep_find_dfs(val, key)

            if result:
                return result

        if isinstance(val, (list, set, tuple)):
            for elem in val:
                result = deep_find_dfs(elem, key)

                if result is not None:
                    return result


if __name__=='__main__':
    some_dict = {
    'a': 1,
    'b': {
        'c': 3,
        'd': [{'e': 5}],
        'f': {
            'g': 6
        }
    }
}

    print(deep_find_dfs(some_dict, 'a') == some_dict['a'])
    print(deep_find_dfs(some_dict, 'b') == some_dict['b'])
    print(deep_find_dfs(some_dict, 'c') == some_dict['b']['c'])
    print(deep_find_dfs(some_dict, 'd') == some_dict['b']['d'])
    print(deep_find_dfs(some_dict, 'e') == some_dict['b']['d'][0]['e'])
    print(deep_find_dfs(some_dict, 'f') == some_dict['b']['f'])
    print(deep_find_dfs(some_dict, 'g') == some_dict['b']['f']['g'])
    print(deep_find_dfs(some_dict, 'shano') == None)