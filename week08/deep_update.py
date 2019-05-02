def deep_update(data, key, val):
    for k, v in data.items():
        if k == key:
            data[k] = val
        elif isinstance(v, (list,set,tuple)):
            for elem in v:
                deep_update(elem, key, val)
        if isinstance(v,dict):
            deep_update(v, key, val)
    return data
