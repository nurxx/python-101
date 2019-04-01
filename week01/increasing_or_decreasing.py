def increasing_or_decreasing(seq):

    increasing=sorted(list(set(seq)))
    decreasing=sorted(list(set(seq)))

    if increasing == seq:
        return 'Up!'
    elif list(reversed(decreasing))==seq:
        return 'Down!'
    else:
        return False
