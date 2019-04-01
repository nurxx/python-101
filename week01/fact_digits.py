def factorial(num):
    f=1
    while num!=1:
        f*=num
        num=num-1
    return f


def fact_digits(n):
    l=[]
    while n:
        l=l+[n%10]
        n=n//10

    sum=0
    for i in l:
        sum+=factorial(i)
    print(sum)
