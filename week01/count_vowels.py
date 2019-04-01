# def count_vowels(string):
#     vowels=0
#     string=string.lower()
#     for i in string:
#         if i=='o' or i=='u' or i=='e' or i=='a' or i=='y' or i=='i':
#             vowels+=1
#     return vowels

def count_vowels(string):
    vowels='aeiouy'
    count=0
    for i in string:
        if lower(i) in vowels:
            count+=1
    return count