from cashdesk import *
import unittest 

class TestCashDesk(unittest.TestCase):
    def test_when_initialize_and_print_bill(self):
        bill = Bill(100)
        expected_result = "A 100$ bill"
        self.assertEqual(repr(bill),expected_result)

    def test_when_validate_input_params_for_bill_with_negative_amount(self):
        with self.assertRaises(ValueError):
            bill = Bill(-30)
        
    def test_when_validate_input_params_for_bill_with_non_integer_amount(self):
        with self.assertRaises(TypeError):
            bill = Bill('20')

    def test_when_compare_two_bills(self):
        bill_1= Bill(120)
        bill_2 = Bill(120)
        self.assertEqual(bill_1,bill_2)

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
        bills= [20,10,10,10,70,90,90]
        batch=BatchBill([Bill(x) for x in bills])
        expected_result = 7
        self.assertEqual(len(batch),expected_result)
    
    def test_when_getting_total_bills_amount_of_batch_bill(self):
        values= [10,20,50,100]
        bills = [Bill(value) for value in values]
        batch = BatchBill(bills)
        expected_result = 180
        self.assertEqual(batch.total(),expected_result)

    def test_when_adding_bill_to_cash_desk(self):
        desk = CashDesk()
        desk.take_money(Bill(10))
        expected_result = {Bill(10): 1}
        self.assertEqual(desk.table,expected_result)

    def test_when_adding_batch_bills_to_cash(self):
        values = [10, 20, 50, 100, 100, 100]
        bills = [Bill(value) for value in values]
        batch = BatchBill(bills)
        desk = CashDesk()
        desk.take_money(batch)
        expected_result = {Bill(10):1,Bill(20):1,Bill(50):1,Bill(100):3}
        self.assertEqual(desk.table,expected_result)

    def test_when_inspect_cash(self):
        values = [10, 20, 50, 100, 100, 100]
        bills = [Bill(value) for value in values]
        batch = BatchBill(bills)
        desk = CashDesk()
        desk.take_money(batch)
        expected_result = {Bill(10):1,Bill(20):1,Bill(50):1,Bill(100):3}
        self.assertEqual(desk.table,expected_result)
        
if __name__=='__main__':
    unittest.main()