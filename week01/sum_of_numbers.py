import re 

def sum_of_numbers(input_string):
    integers= re.findall(r"\d+",input_string)
    integers=list(map(int,integers))
    return sum(integers)


