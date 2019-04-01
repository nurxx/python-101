def anagrams():
    input_strings=list(map(str,input().split()))
    input_strings=[string.lower() for string in input_strings]
    if len(input_strings[0])!=len(input_strings[1]):
        return 'NOT ANAGRAMS'

    return 'ANAGRAMS' if str(sorted(input_strings[0]))==str(sorted(input_strings[1])) else 'NOT ANAGRAMS'

