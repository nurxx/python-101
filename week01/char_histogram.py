def char_histogram(string):
    result={}

    for ch in string:
        if ch not in result:
            result[ch]=0

        result[ch]+=1
    return result