
def group(llist):
    result=[]
    i=0
    while i < len(llist):
        sublist=[]
        j=i
        while j < len(llist) and llist[i]==llist[j]:
                sublist+= [llist[j]]
                j+=1

        result+=[sublist]
        i+=j-i
    return result







