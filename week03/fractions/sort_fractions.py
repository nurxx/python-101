def get_key(fraction):
    return fraction[0]/fraction[1]

def sort_fractions(fractions):
    return sorted(fractions,key=get_key)