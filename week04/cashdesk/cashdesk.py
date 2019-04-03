class TypeError(Exception):
    pass

class ValueError(Exception):
    pass

class Bill:
    def __init__(self,amount):
        self.validate_init_params(amount)
        self.amount = amount

    def validate_init_params(self,amount):
        if type(amount) is not int:
            raise TypeError('Type must be an integer!')
        if amount < 0:
            raise ValueError('Bill cannot have negative amount!')

    def __str__(self):
        return 'A {}$ bill'.format(self.amount)

    def __eq__(self,other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.amount)*7

    def __repr__(self):
        #return 'Bill : {}'.format(self.amount)
        return self.__str__()

    def __int__(self):
        return int(self.amount)

class BatchBill:
    def __init__(self,bills):
        self.validate_batch_bills(bills)
        self.bills = bills

    def validate_batch_bills(self,bills):
        if type(bills) is not list:
            raise TypeError('BatchBills type must be a list!')

        for bill in bills:
            if type(bill) is not Bill:
                raise TypeError('Bill type must be an integer!')

    def __len__(self):
        return len(self.bills)

    def __getitem__(self, index):
        return self.bills[index]

    def total(self):
        total_amount_in_batch=0
        for bill in self.bills:
            total_amount_in_batch+=bill.amount
        return total_amount_in_batch

class CashDesk:
    def __init__(self):
        self.table= dict()

    def take_money(self,money):
        if type(money) is Bill:
            if money in self.table:
                self.table[money] += 1
            else:
                self.table[money] = 1
        elif type(money) is BatchBill:
            for bill in money:
                if bill in self.table:
                    self.table[bill]+=1
                else:
                    self.table[bill] = 1

    def total(self):
        total_amount = 0
        for key,value in self.table.items():
            total_amount += key.amount*value
        return total_amount

    def inspect(self):
        for key,value in self.table.items():
            print(key,value)
        return self.table

if __name__=='__main__':
    values= [10,20,50,100]
    bills = [Bill(value) for value in values]
    batch =BatchBill(bills)
    for bill in batch:
        print(bill)

    values = [10, 20, 50, 100, 100, 100]
    bills = [Bill(value) for value in values]

    batch = BatchBill(bills)

    desk = CashDesk()

    desk.take_money(batch)
    desk.take_money(Bill(10))

    print(desk.total()) # 390
    desk.inspect()