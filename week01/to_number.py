# def to_number(digits):
#     result=''
#     for i in digits:
#         result+=str(i)
#     print(int(result))

#2nd solution
def to_number(digits):
    return int(join(str(ch) for ch in digits))