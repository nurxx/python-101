from parse_money_tracker_data import *
from money_tracker import *
from aggregated_money_tracker import *
import unittest

class TestMoneyTracker(unittest.TestCase):
    def test_when_init_income(self):
        income = Income(120,'Salary','=== 25-03-2018 ===')
        expected_result = 'An income with : amount 120 : subcategory Salary : date === 25-03-2018 ==='
        self.assertTrue(income,expected_result)

    def test_when_init_expense(self):
        expense = Expense(1500,"Cat's needs",'=== 13-06-2019 ===')
        expected_result = "An expense with : amount 1500 : subcategory Cats's needs : date === 13-06-2019 ==="
        self.assertTrue(expense,expected_result)

    def test_when_initializing_aggregated_money_tracker(self):
        data = [['=== 22-03-2019 ===\n', '760, Salary, New Income\n','14, Pets, New Expense\n','21.5, Transport, New Expense\n'],
                ['=== 23-03-2019 ===\n', '50, Savings, New Income\n', '15, Food, New Expense\n' '200, Deposit, New Income\n']]
        expected_incomes =['An income with : amount 760 : subcategory Salary : date === 22-03-2019 ===',
                            'An income with : amount 50 : subcategory Savings : date === 23-03-2019 ===',
                            'An income with : amount 200 : subcategory Deposit : date === 23-03-2019 ===']
        expected_expenses = ['An expense with : amount 14 : subcategory Pets : date === 22-03-2019 ===',
                            'An expense with : amount 21.5 : subcategory Transport : date === 22-03-2019 ===',
                            'An expense with : amount 15 : subcategory Food : date === 23-03-2019 ===']
        aggregated_money_tracker_data = AggregatedMoneyTracker(data)
        self.assertTrue(aggregated_money_tracker_data.incomes,expected_incomes)
        self.assertTrue(aggregated_money_tracker_data.expenses,expected_expenses)

    def test_when_print_expenses_in_aggregated_data_and_show_user_expenses(self):
        data = [['=== 22-03-2019 ===\n', '760, Salary, New Income\n','14, Pets, New Expense\n','21.5, Transport, New Expense\n'],
                ['=== 23-03-2019 ===\n', '50, Savings, New Income\n', '15, Food, New Expense\n' '200, Deposit, New Income\n']]
        expected_result = ['An expense with : amount 14 : subcategory Pets : date === 22-03-2019 ===',
                            'An expense with : amount 21.5 : subcategory Transport : date === 22-03-2019 ===',
                            'An expense with : amount 15 : subcategory Food : date === 23-03-2019 ===']
        aggregated_money_tracker_data = AggregatedMoneyTracker(data)
        self.assertTrue(aggregated_money_tracker_data.print_expenses(),expected_result)

    def test_when_print_incomes_in_aggregated_data_and_show_user_incomes(self):
        data = [['=== 22-03-2019 ===\n', '760, Salary, New Income\n','14, Pets, New Expense\n','21.5, Transport, New Expense\n'],
                ['=== 23-03-2019 ===\n', '50, Savings, New Income\n', '15, Food, New Expense\n' '200, Deposit, New Income\n']]
        expected_incomes =['An income with : amount 760 : subcategory Salary : date === 22-03-2019 ===',
                            'An income with : amount 50 : subcategory Savings : date === 23-03-2019 ===',
                            'An income with : amount 200 : subcategory Deposit : date === 23-03-2019 ===']
        aggregated_money_tracker_data = AggregatedMoneyTracker(data)
        self.assertTrue(aggregated_money_tracker_data.print_incomes(),expected_incomes)

    def test_when_showing_data_per_date(self):
        data = [['=== 22-03-2019 ===\n', '760, Salary, New Income\n','14, Pets, New Expense\n','21.5, Transport, New Expense\n'],
                ['=== 23-03-2019 ===\n', '50, Savings, New Income\n', '15, Food, New Expense\n' '200, Deposit, New Income\n']]
        date = '23-03-2019'
        expected_result = ['An income with : amount 50 : subcategory Savings : date === 23-03-2019 ===',
                            'An income with : amount 200 : subcategory Deposit : date === 23-03-2019 ===',
                            'An expense with : amount 15 : subcategory Food : date === 23-03-2019 ===']
        money_tracker = MoneyTracker(AggregatedMoneyTracker(data))
        self.assertTrue(money_tracker.show_data_for_specific_date(date),expected_result)
    
    def test_when_showing_expenses_ordered_by_subcategories(self):
        data = [['=== 22-03-2019 ===\n', '760, Salary, New Income\n','14, Pets, New Expense\n','21.5, Transport, New Expense\n'],
                ['=== 23-03-2019 ===\n', '50, Savings, New Income\n', '15, Food, New Expense\n' '200, Deposit, New Income\n']]
                            
        expected_result = ['An expense with : amount 15 : subcategory Food : date === 23-03-2019 ===',
                            'An expense with : amount 14 : subcategory Pets : date === 22-03-2019 ===',
                            'An expense with : amount 21.5 : subcategory Transport : date === 22-03-2019 ===']
        money_tracker = MoneyTracker(AggregatedMoneyTracker(data))
        self.assertTrue(money_tracker.show_expenses_ordered_by_subcategories(),expected_result)

    def test_when_showing_incomes_in_reverse_order_by_subcategories(self):
        data = [['=== 22-03-2019 ===\n', '760, Salary, New Income\n','14, Pets, New Expense\n','21.5, Transport, New Expense\n'],
                ['=== 23-03-2019 ===\n', '50, Savings, New Income\n', '15, Food, New Expense\n' '200, Deposit, New Income\n']]

        expected_incomes =['An income with : amount 50 : subcategory Savings : date === 23-03-2019 ===',
                            'An income with : amount 760 : subcategory Salary : date === 22-03-2019 ===',
                            'An income with : amount 200 : subcategory Deposit : date === 23-03-2019 ===']
        money_tracker = MoneyTracker(AggregatedMoneyTracker(data))
        self.assertTrue(money_tracker.show_incomes_in_reverse_order_by_subcategories(),expected_incomes)

    def test_when_adding_new_income_with_existing_date_in_money_tracker(self):
        data = [['=== 22-03-2019 ===\n', '760, Salary, New Income\n','14, Pets, New Expense\n','21.5, Transport, New Expense\n'],
                ['=== 23-03-2019 ===\n', '50, Savings, New Income\n', '15, Food, New Expense\n' '200, Deposit, New Income\n']]

        money_tracker = MoneyTracker(AggregatedMoneyTracker(data))
        money_tracker.add_new_income(200,'Salary','=== 23-03-2019 ===')
        expected_result =['An income with : amount 50 : subcategory Savings : date === 23-03-2019 ===',
                            'An income with : amount 200 : subcategory Deposit : date === 23-03-2019 ===',
                            'An expense with : amount 15 : subcategory Food : date === 23-03-2019 ===',
                            'An income with : amount 200 : subcategory Salary : data === 23-03-2019 ===']
        date = '23-03-2019'
        self.assertTrue(money_tracker.show_data_for_specific_date(date),expected_result)

    def test_when_adding_new_income_with_not_present_date(self):
        data = [['=== 22-03-2019 ===\n','50, Savings, New Income\n']]
        money_tracker = MoneyTracker(AggregatedMoneyTracker(data))
        money_tracker.add_new_income(200,'Salary','=== 23-03-2019 ===')

        expected_result = ['An income with : amount 200 : subcategory Salary : data === 23-03-2019 ===']
        date = '23-03-2019'
        self.assertTrue(money_tracker.show_data_for_specific_date(date),expected_result)

    def test_when_adding_new_expense_with_existing_date_in_money_tracker(self):
        data = [['=== 22-03-2019 ===\n', '760, Salary, New Income\n','14, Pets, New Expense\n','21.5, Transport, New Expense\n'],
                ['=== 23-03-2019 ===\n', '50, Savings, New Income\n', '15, Food, New Expense\n' '200, Deposit, New Income\n']]

        money_tracker = MoneyTracker(AggregatedMoneyTracker(data))
        money_tracker.add_new_expense(200,'Cat Food','=== 23-03-2019 ===')
        expected_result =['An income with : amount 50 : subcategory Savings : date === 23-03-2019 ===',
                            'An income with : amount 200 : subcategory Deposit : date === 23-03-2019 ===',
                            'An expense with : amount 15 : subcategory Food : date === 23-03-2019 ===',
                            'An expense with : amount 200 : subcategory Cat Food : data === 23-03-2019 ===']
        date = '23-03-2019'
        self.assertTrue(money_tracker.show_data_for_specific_date(date),expected_result)

    def test_when_adding_new_expense_with_not_present_date(self):
        data = [['=== 22-03-2019 ===\n','50, Savings, New Income\n']]
        money_tracker = MoneyTracker(AggregatedMoneyTracker(data))
        money_tracker.add_new_expense(200,'Cat Needs','=== 23-03-2019 ===')

        expected_result = ['An expense with : amount 200 : subcategory Cat Needs : data === 23-03-2019 ===']
        self.assertTrue(money_tracker.show_expenses_ordered_by_subcategories(),expected_result)
    
if __name__ == '__main__':
    unittest.main()
