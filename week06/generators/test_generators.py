import unittest
from generators import *

class TestGenerators(unittest.TestCase):
    def test_chain_generator(self):
        expected_result = (0,1,2,3,3,4,5,6)
        self.assertEqual(expected_result,tuple(chain(range(0,4),range(3,7))))

    def test_compress_generator(self):
        expected_result = {'Panda'}
        self.assertEqual(expected_result,set(compress(["Ivo", "Rado", "Panda"], [False, False, True])))


if __name__ == '__main__':
    unittest.main()