import unittest 
from decorators import *

class TestDecorators(unittest.TestCase):
    def test_validation_accepts_decorator(self):
        @accepts(str,int)
        def years(name,year):
            return 'My {0} is {1} years old.'.format(name,year)

        with self.assertRaises(TypeError):
            panda = years('HackPanda','three')

    def test_accepts_decorator_with_one_argument(self):
        @accepts(str)
        def say_hello(name):
            return 'Hello, {0}.'.format(name)

        panda = say_hello('HackPanda')
        self.assertEqual('Hello, HackPanda.',panda)

    def test_accepts_decorator_with_more_than_one_arguments(self):
        @accepts(str, int)
        def deposit(name, money):
            print("{} sends {} $!".format(name, money))
            return True

        rozas_deposit = deposit('Roza',10)
        self.assertTrue(True,rozas_deposit)

    def test_encrypt_decorator_without_function_arguments(self):
        @encrypt(3)
        def get_low():
            return 'Get get get low!'

        encrypted = get_low()
        self.assertEqual('Jhw jhw jhw orz!', encrypted)

    def test_nested_log_and_encrypt_decorator(self):
        @log('log.txt')
        @encrypt(3)
        def get_low():
            return "Get get get low"

        encrypted = get_low()
        with open('log.txt','r') as f:
            lines = f.readlines()
        self.assertTrue(lines[-1],'get_low was called at {}'.format(datetime.datetime.now()))

    def test_performance_decorator(self):
        @performance('log.txt')
        def something_heavy():
            sleep(2)
            return "I am done!"

        called = something_heavy()
        with open('log.txt','r') as f:
            lines = f.readlines()
        self.assertTrue(lines[-1],'something_heavy was called and took {} seconds to execute'.format('%.2f'%(time()-start_time)))


if __name__ == '__main__':
    unittest.main()