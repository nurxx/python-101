import unittest
from money_tracker import *

class TestingMoneyTracker(unittest.TestCase):
    def test_when_listing_user_data(self):
        input_data = {'22-03-2019': {'income': [(760.0,'Salary')],'expense': [(5.5, 'Eating Out'),
        (112.4, 'Bills'), (21.5, 'Transport')]},'23-03-2019': {'income': [(50.0, 'Savings'),
        (200.0, 'Deposit')],'expense': [(15.0, 'Food'), (5.0, 'Sports')]}}
        expected_result = {'22-03-2019': {'income': [(760.0,'Salary')],'expense': [(5.5, 'Eating Out'),
        (112.4, 'Bills'), (21.5, 'Transport')]},'23-03-2019': {'income': [(50.0, 'Savings'),
        (200.0, 'Deposit')],'expense': [(15.0, 'Food'), (5.0, 'Sports')]}}
        self.assertEqual(list_user_data(input_data),expected_result)

    def test_when_showing_user_incomes(self):
        input_data = {'22-03-2019': {'income': [(10, 'Deposit')], 'expense': [(27.7, 'Food')]},
        '23-03-2019': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'Eating Out')]}}
        expected_result = [(10, 'Deposit'), (50, 'Savings'), (700, 'Salary')]
        self.assertEqual(show_user_incomes(input_data),expected_result)

    def test_when_showing_user_expenses(self):
        input_data = {'22-03-2019': {'income':[(10,'Savings'),(20,'Savings')],'expense':[]},
        '24-03-2019':{'income': [(12,'Deposit')],'expense':[(85.9,'Food'),(30,'Transport')]}}
        expected_result = [(30,'Transport'),(85.9,'Food')]
        self.assertEqual(show_user_expenses(input_data),expected_result)

    def test_when_listing__user_expenses_ordered_by_categories(self):
        input_data = {'22-03-2019': {'expense': [(5.5, 'Eating Out'), (34.0, 'Clothes'), (41.79, 'Food'), 
        (12.0, 'Eating Out'),(7.0, 'House'), (14.0, 'Pets'), (112.4, 'Bills'), (21.5, 'Transport')],
        'income': [(760.0, 'Salary')]},'23-03-2019': {'expense': [(15.0, 'Food'), (5.0, 'Sports')],
        'income': [(50.0, 'Savings'), (200.0, 'Deposit'),(10.0, 'Deposit')]}}
        expected_result = [(112.40, 'Bills'), (34, 'Clothes'), (5.5, 'Eating Out'), (12, 'Eating Out'),
        (15, 'Food'), (41.79, 'Food'), (7, 'House'), (14, 'Pets'), (5, 'Sports'), (21.5, 'Transport')]
        self.assertEqual(list_user_expenses_ordered_by_categories(input_data),expected_result)

    def test_when_showing_user_data_per_date(self):
        input_data = {'22-03-2019': {'expense': [(5.5, 'Eating Out'), (34.0, 'Clothes'), (41.79, 'Food'), 
        (12.0, 'Eating Out'),(7.0, 'House'), (14.0, 'Pets'), (112.4, 'Bills'), (21.5, 'Transport')],
        'income': [(760.0, 'Salary')]},'23-03-2019': {'expense': [(15.0, 'Food'), (5.0, 'Sports')],
        'income': [(50.0, 'Savings'), (200.0, 'Deposit'),(10.0, 'Deposit')]}}
        specific_date = '23-03-2019'
        expected_result = {'expense':[(15.0, 'Food'),(5.0, 'Sports')],'income':[(50.0, 'Savings'),
        (200.0, 'Deposit'),(10.0, 'Deposit')]}
        self.assertEqual(show_user_data_per_date(specific_date,input_data),expected_result)

    def test_when_listing_income_categories(self):
        input_data = {'22-03-2019': {'expense': [(5.5, ' Eating Out'), (34.0, ' Clothes'), (41.79, ' Food'),
        (12.0, ' Eating Out'), (7.0, ' House'), (14.0, ' Pets'), (112.4, ' Bills'), (21.5, ' Transport')],
        'income': [(760.0, ' Salary')]}, '23-03-2019': {'expense': [(15.0, ' Food'), (5.0, ' Sports')],
        'income': [(50.0, ' Savings'), (200.0, ' Deposit'), (10.0, ' Deposit')]}}
        expected_result = [' Deposit', ' Salary', ' Savings']
        self.assertEqual(list_income_categories(input_data),expected_result) 

    def test_when_listing_expense_categories(self):
        input_data = {'22-03-2019': {'expense': [(5.5, ' Eating Out'), (34.0, ' Clothes'), (41.79, ' Food'),
        (12.0, ' Eating Out'), (7.0, ' House'), (14.0, ' Pets'), (112.4, ' Bills'), (21.5, ' Transport')],
        'income': [(760.0, ' Salary')]}, '23-03-2019': {'expense': [(15.0, ' Food'), (5.0, ' Sports')],
        'income': [(50.0, ' Savings'), (200.0, ' Deposit'), (10.0, ' Deposit')]}}
        expected_result = [' Bills',' Clothes',' Eating Out',' Food',' House',' Pets',' Sports',' Transport']
        self.assertEqual(list_expense_categories(input_data),expected_result)

    def test_when_adding_new_income(self):
        input_data = {'22-03-2019': {'income': [(10, 'Deposit')], 'expense': [(27.7, 'Food')]},
        '23-03-2019': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'Eating Out')]}}
        income_category = 'Part-time Work'
        money = 115
        date = '23-03-2019'
        expected_result = {'income':[(700,'Salary'),(50,'Savings'),(115,'Part-time Work')], 
        'expense': [(4, 'Eating Out')]}
        self.assertEqual(show_user_data_per_date('23-03-2019',add_income(income_category,money,date,input_data)),expected_result)

    def test_when_adding_new_expense(self):
        input_data = {'22-03-2019': {'income': [(10, 'Deposit')], 'expense': [(27.7, 'Food')]},
        '23-03-2019': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'Eating Out')]}}
        expense_category = 'Pets'
        money = 23.4
        date = '25-03-2019'
        expected_result = ['Eating Out','Food','Pets']
        self.assertEqual(list_expense_categories(add_expense(expense_category,money,date,input_data)),expected_result)


if __name__ == '__main__':
    unittest.main()