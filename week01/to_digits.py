#Standard algo

# def to_digits(num):
#     l=[]
#     while num:
#         l.append(num%10)
#         num=num//10
#     result=list(reversed(l))
#     print(result)

#Python
def to_digits(num):
    num=abs(num)
    return [int(ch) for ch in str(num)]
