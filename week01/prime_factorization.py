
def prime_factorization(n):
    count=0
    llist=list()
    copy_n=n
    while n%2==0:
        n//=2
        count+=1

    if count != 0:
        llist.append((2,count))

    for i in range(3,n+1,2):
        count=0
        if n%i==0:
            print('yes')
            while n%i==0:
                n//=i
                count+=1
            if count!=0:
                llist.append((i,count))

    return llist
