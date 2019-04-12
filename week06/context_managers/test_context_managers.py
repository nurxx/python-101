import unittest 
from performance import *
from assert_raises import *
import time
import datetime

class TestContextManagers(unittest.TestCase):
    def test_performance_context_manager(self):
        def get_low():
            time.sleep(7)
            return 'Get low!'
        date = datetime.datetime.now()
        start = time.time()
        with open('performance.txt','r') as f:
            lines = f.readlines()

        with performance('performance.txt'):
            get_low()

        with open('performance.txt','r') as f:
            result = f.readlines()

        self.assertEqual(len(lines)+1,len(result))

    def test_assert_raises_context_manager_when_exception_raised_return_true(self):
        def sum(a,b):
            if type(a) is str or type(b) is str:
                raise TypeError('Str type not allowed!')
            return True

        with assertRaises(TypeError,'Str type not allowed!'):
            self.assertEqual(True,sum('1',1))



if __name__ == '__main__':
    unittest.main()