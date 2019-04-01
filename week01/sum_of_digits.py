# def sum_of_digits(num):
#     if num < 0:
#         num=-num
#     sum=0
#     while num :
#         sum=sum+ (num%10)
#         num=num//10
#     print(sum)

def sum_of_digits(num):
    num=abs(num)
    digits=[int(x) for x in str(num)]
    return sum(digits)