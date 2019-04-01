class Category:
    def __init__(self,amount,sub_category,date):
        self.amount = amount
        self.sub_category = sub_category
        self.date = date

    def __str__(self):
        return 'A category with : amount {0} : subcategory {1} : date {2}'.format(self.amount,self.sub_category,self.date)

    def __repr__(self):
        return self.__str__()

    def __eq__(self,other):
        return self.amount == other.amount and self.sub_category == other.sub_category and self.date == other.date

class Income(Category):
    __type_category = 'income'
    def __init__(self,amount,sub_category,date):
        super().__init__(amount,sub_category,date)

    def __str__(self):
        return 'An income with : amount {0} : subcategory {1} : date {2}'.format(self.amount,self.sub_category,self.date)

    def __repr__(self):
        return self.__str__()

class Expense(Category):
    __type_category = 'expense'
    def __init__(self,amount,sub_category,date):
        super().__init__(amount,sub_category,date)

    def __str__(self):
        return 'An expense with : amount {0} : subcategory {1} : date {2}'.format(self.amount,self.sub_category,self.date)

    def __repr__(self):
        return self.__str__()

 