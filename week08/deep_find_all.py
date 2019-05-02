def deep_find_all_dfs(data, key, found_values = []):
    for k, v in data.items():
        if k == key:
            found_values.append(v)

        if isinstance(v, dict):
            deep_find_all_dfs(v, key, found_values)
        elif isinstance(v, (list,set,tuple)):
            for elem in v:
                deep_find_all_dfs(elem, key, found_values)
    return found_values
