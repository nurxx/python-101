import unittest 
from cashdesk import *

class TestCashDesk(unittest.TestCase):
    def setUp(self):
        self.bill= Bill(100)
        bills= [10,20,50,50,50,100,100]
        self.batch=BatchBill([Bill(bill) for bill in bills])
    
    def test_when_initialize_and_print_bill(self):
        expected_result = "A 100$ bill"
        self.assertEqual(repr(self.bill),expected_result)

    def test_when_validate_input_params_for_bill_with_negative_amount(self):
        with self.assertRaises(ValueError):
            bill = Bill(-30)
        
    def test_when_validate_input_params_for_bill_with_non_integer_amount(self):
        with self.assertRaises(TypeError):
            bill = Bill('20')

    def test_when_compare_two_bills(self):
        self.assertEqual(self.bill,self.bill)

    def test_when_initialize_batch_bills_including_non_integer_bill(self):
        bills = [10,20,50,50,80,'20']
        with self.assertRaises(TypeError):
            batch_bills = [Bill(x) for x in bills]
            batch = BatchBill(batch_bills)

    def test_when_initialize_batch_bills_including_bill_with_negative_amount(self):
        bills = [10,20,50,50,80,-20]
        with self.assertRaises(ValueError):
            batch_bills = [Bill(x) for x in bills]
            batch = BatchBill(batch_bills)

    def test_count_bills_in_batch_bill(self):
        expected_result = 7
        self.assertEqual(len(self.batch),expected_result)
    
    def test_when_getting_total_bills_amount_of_batch_bill(self):
        expected_result = 380
        self.assertEqual(self.batch.total(),expected_result)

    def test_when_adding_bill_to_cash_desk(self):
        desk = CashDesk()
        desk.take_money(self.bill)
        expected_result = {Bill(100): 1}
        self.assertEqual(desk.table,expected_result)

    def test_when_adding_batch_bills_to_cash(self):
        desk = CashDesk()
        desk.take_money(self.batch)
        expected_result = {Bill(50):3,Bill(100):2,Bill(10):1,Bill(20):1}
        self.assertEqual(desk.table,expected_result)

    def test_when_inspect_cash(self):
        desk = CashDesk()
        desk.take_money(self.batch)
        expected_result = {Bill(10):1,Bill(20):1,Bill(50):3,Bill(100):2}
        self.assertEqual(desk.table,expected_result)
        
if __name__=='__main__':
    unittest.main()