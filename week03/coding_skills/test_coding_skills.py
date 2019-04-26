import unittest 
from coding_skills import *

class TestCodingSkills(unittest.TestCase):
    def test_file_input(self):
        filename = 'data.json'
        with open(filename,'r') as f:
            data = json.load(f)
        self.assertTrue(type(data),type(dict()))

    def test_conding_skills(self):
        filename = 'data.json'
        expected_data = {'C++': [(99, 'Cherna Ninja')], 'PHP': [(37, 'Rado Rado')],
                         'Python': [(80, 'Ivo Ivo')], 'C#': [(70, 'Pavli Pavli')],
                         'Haskell': [(70, 'Rado Rado')], 'Java': [(50, 'Rado Rado')],
                         'JavaScript': [(62, 'Rosi Rosi')], 'Ruby': [(35, 'Rosi Rosi')],
                         'CSS': [(99, 'Pavli Pavli')], 'C': [(99, 'Cherna Ninja')]}
        self.assertTrue(coding_skills(filename),expected_data)

if __name__ == '__main__':
    unittest.main()