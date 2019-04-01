from group import group

def max_consecutive(items):
    return max([len(item) for item in group(items)])
    