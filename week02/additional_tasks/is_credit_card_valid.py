def is_credit_card_valid(number):
    number=list(map(int,str(number)))
    number=[number[i]*2 if i%2!=0 else number[i] for i in range(len(number))]
    number=''.join(map(str,number))
    
    return sum(list(map(int,number)))%10==0 and len(number)%2!=0
