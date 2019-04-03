from category import *
from parse_money_tracker_data import *

class AggregatedMoneyTracker:
    def __init__(self,data):
        self.incomes = []
        self.expenses = []
        for index,item in enumerate(data):
            date = data[index][0].strip('\n')
            date = data[index][0].strip()
            for index,elem in enumerate(item):
                elem = elem.strip('\n')
                elem = elem.split(', ')
                if 'New Income' in elem:
                    self.incomes += [Income(elem[0],elem[1],date)]
                if 'New Expense' in elem:
                    self.expenses += [Expense(elem[0],elem[1],date)]

    def print_incomes(self):
        for income in self.incomes:
            print(income)
        return self.incomes

    def print_expenses(self):
        for expense in self.expenses:
            print(expense)
        return self.expenses
