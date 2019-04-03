from aggregated_money_tracker import *

class TypeError(Exception):
    pass

class MoneyTracker:
    def __init__(self,aggregated_data):
        self.validate_input_params(aggregated_data)

        self.aggregated_data = aggregated_data
    def validate_input_params(self,aggregated_data):
        if type(aggregated_data) is not AggregatedMoneyTracker:
            raise TypeError('Type of data must be < AggregatedMoneyTracker > !')

    def show_all_data(self):
        self.aggregated_data.print_incomes()
        self.aggregated_data.print_expenses()

    def show_data_for_specific_date(self,date):
        result = list()
        for income in self.aggregated_data.incomes:
            if date in income.date:
                print(income)
                result.append(income)
        for expense in self.aggregated_data.expenses:
            if date in expense.date:
                print(expense)
                result.append(expense)
        return result

    def show_expenses_ordered_by_subcategories(self):
        ordered_expenses = sorted(self.aggregated_data.expenses,key= lambda object: object.sub_category)
        for expense in ordered_expenses:
            print(expense)
        return ordered_expenses

    def show_incomes_in_reverse_order_by_subcategories(self):
        ordered_incomes = sorted(self.aggregated_data.incomes, key = lambda object: object.sub_category,reverse = True)
        for income in ordered_incomes:
            print(income)
        return ordered_incomes

    def add_new_income(self,amount,sub_category,date):
        self.aggregated_data.incomes += [Income(str(amount),sub_category,date)]

    def add_new_expense(self,amount,sub_category,date):
        self.aggregated_data.expenses += [Expense(str(amount),sub_category,date)]

    def show_user_incomes(self):
        self.aggregated_data.print_incomes()

    def show_user_expenses(self):
        self.aggregated_data.print_expenses()
