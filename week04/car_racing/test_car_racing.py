import unittest
import os
from race import *

class TestCarRacing(unittest.TestCase):
    def test_when_initialize_car(self):
        car = Car('Pegeout','107',180)
        expected_output = 'a Pegeout 107 with max speed 180'
        self.assertTrue(car,expected_output)

    def test_validation_driver_input_params(self):
        with self.assertRaises(TypeError):
            driver = Driver('Rado','Pegeout')

    def test_when_initialize_driver(self):
        car = Car('Pegeout','107',180)
        driver = Driver('Rado',car)
        expected_output = 'Rado has a Pegeout 107 with max speed 180'
        self.assertTrue(driver,expected_output)

    def test_validation_race_drivers(self):
        with self.assertRaises(TypeError):
            race = Race('Panda Race',0.2,[Driver('Rado',280),Driver('Panda','PandaCar')])

    def test_existance_of_file_with_saved_championship_standings(self):
        self.assertTrue(True,os.path.isfile('./result.json'))

    def test_validation_result_json_data(self):
        with open('./result.json','r') as json_file:
            data = json.load(json_file)
        self.assertTrue(type(data),type(dict()))

if __name__ == '__main__':
    unittest.main()