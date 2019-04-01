# def count_consonants(string):
#     consonants=0
#     string=string.lower()
#     for i in string:
#         if i!='o' and i!='u' and i!='e' and i!='a' and i!='y' and i!='i' and i.isalpha()==True:
#             consonants+=1
#     return consonants

def count_consonants(string):
    count=0
    vowels='aeiouy'
    for i in string:
        if lower(i) not in vowels and lower(i).isalpha():
            count+=1
    return count