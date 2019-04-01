from filter import *
from count import *
from first import *
from last import *

import unittest

class TestFilter(unittest.TestCase):
    def test_when_filter_by_one_argument(self):
        expected_result = [['Diana Harris','lime','Martin-Barnes','timothy81@gmail.com','1-860-251-9980x6941','5354']]
        self.assertEqual(filter('example_data.csv',full_name='Diana Harris'),expected_result)

    def test_when_filter_by_more_than_one_argument(self):
        expected_result = [['Deborah Lopez','blue','Henson-Pearson','mclaughlintony@gmail.com','(783)023-6489','5067']]
        self.assertEqual(filter('example_data.csv',full_name = 'Deborah Lopez',favourite_color = 'blue',company_name = 'Henson-Pearson'),expected_result)

    def test_when_filter_by_full_name_startswith(self):
        expected_result = [['Mr. Larry Wu DDS','fuchsia',"Schroeder, Huynh and Wagner",'ngarza@hotmail.com','107.259.2586x18510','4491'],
                            ['Mr. Henry Bell MD','gray',"Gallegos, Ortiz and Robinson",'eyates@gmail.com','1-449-374-8755','8479'],
                            ['Mr. Austin Reid','blue','Daniel-Guzman','donnadaniels@yahoo.com','427.328.7666','6104'],
                            ['Mr. Calvin Nelson','olive','Aguirre-Forbes','kara23@hotmail.com','05505177198','3736']]
        self.assertEqual(filter('example_data.csv',full_name__startswith='Mr.'),expected_result)

    def test_when_filter_by_contains_and_startswith_combined(self):
        expected_result =[['Mr. Calvin Nelson','olive','Aguirre-Forbes','kara23@hotmail.com','05505177198','3736']]
        self.assertEqual(filter('example_data.csv',full_name__startswith='Mr.',full_name__contains='l',email__contains='@hotmail'),expected_result)

    def test_when_filter_by_combined_arguments(self):
        expected_result = [['Mr. Larry Wu DDS','fuchsia',"Schroeder, Huynh and Wagner",'ngarza@hotmail.com','107.259.2586x18510','4491']]
        self.assertEqual(filter('example_data.csv',favourite_color ='fuchsia',full_name__startswith='Mr.',email__contains='@hotmail'),expected_result)

    def test_when_order_by_argument(self):
        expected_result = [['Mr. Austin Reid','blue','Daniel-Guzman','donnadaniels@yahoo.com','427.328.7666','6104'],
                            ['Mr. Larry Wu DDS','fuchsia',"Schroeder, Huynh and Wagner",'ngarza@hotmail.com','107.259.2586x18510','4491'],
                            ['Mr. Henry Bell MD','gray',"Gallegos, Ortiz and Robinson",'eyates@gmail.com','1-449-374-8755','8479'],
                            ['Mr. Calvin Nelson','olive','Aguirre-Forbes','kara23@hotmail.com','05505177198','3736']]
        self.assertEqual(filter('example_data.csv',full_name__startswith='Mr.',order_by='favourite_color'),expected_result)
    def test_when_filter_by_salary_greater_than(self):
        pass

    def test_when_filter_by_salary_less_than(self):
        pass

    def test_when_salary_grater_than_and_less_than_combined(self):
        pass

    def test_when_count_filtered_result(self):
        expected_result = 2
        self.assertEqual(count('example_data.csv',salary='1121'),expected_result)

    def test_when_picking_first_person_from_filtered_result(self):
        expected_result = ['Alan Rangel','maroon','Lee LLC','cmartinez@hotmail.com','(485)723-6325x7701','1121']
        self.assertEqual(first('example_data.csv',salary='1121'),expected_result)

    def test_when_picking_last_person_from_filtered_result(self):
        expected_result = ['Mr. Calvin Nelson','olive','Aguirre-Forbes','kara23@hotmail.com','05505177198','3736']
        self.assertEqual(last('example_data.csv',full_name__startswith='Mr.'),expected_result)

if __name__ == '__main__':
    unittest.main()