def isprime(n):
    if n==1:
        return False
    if n > 1:
        for i in range(2,n):
            if n%i==0:
                return False
    return True

def goldbach(n):
    first=[x for x in range(1,n) if isprime(x)==True]
    second=first
    result=[(x,y) for x in first for y in second if eval('x + y') == n and x <= y]
    return result