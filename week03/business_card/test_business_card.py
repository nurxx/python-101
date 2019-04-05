from business_card import *
import unittest
import os

class TestBusinessCard(unittest.TestCase):
    def test_parsing_json_file(self):
        data = {
    "people": [{
        "first_name": "Ivo",
        "last_name": "Ivo",
        "age": 25,
        "birth_date": "05/05/2005",
        "birth_place": "Sofia",
        "gender": "male",
        "interests": ["eating", "sleeping", "programming", "skiing"],
        "avatar": "ivo.png",
        "skills": [{
            "name": "C++",
            "level": 30
        }, {
            "name": "PHP",
            "level": 25
        }, {
            "name": "Python",
            "level": 80
        }, {
            "name": "C#",
            "level": 25
        }]
    }, {
        "first_name": "Rado",
        "last_name": "Rado",
        "age": 26,
        "birth_date": "06/06/2006",
        "birth_place": "Pleven",
        "gender": "male",
        "interests": ["eating", "sleeping", "programming", "snowboarding"],
        "avatar": "rado.png",
        "skills": [{
            "name": "C++",
            "level": 20
        }, {
            "name": "PHP",
            "level": 37
        }, {
            "name": "Haskell",
            "level": 70
        }, {
            "name": "Java",
            "level": 50
        }, {
            "name": "C#",
            "level": 10
        }, {
            "name": "JavaScript",
            "level": 60
        }]
    }, {
        "first_name": "Rosi",
        "last_name": "Rosi",
        "age": 24,
        "birth_date": "04/04/2004",
        "birth_place": "Sofia",
        "gender": "female",
        "interests": ["eating", "sleeping"],
        "avatar": "rosi.png",
        "skills": [{
            "name": "JavaScript",
            "level": 62
        }, {
            "name": "Python",
            "level": 66
        }, {
            "name": "Ruby",
            "level": 35
        }]
    }, {
        "first_name": "Pavli",
        "last_name": "Pavli",
        "age": 23,
        "birth_date": "03/03/2003",
        "birth_place": "Vratsa",
        "gender": "male",
        "interests": ["eating", "sleeping", "drinking water"],
        "avatar": "pavli.png",
        "skills": [{
            "name": "Python",
            "level": 77
        }, {
            "name": "CSS",
            "level": 99
        }, {
            "name": "JavaScript",
            "level": 33
        }, {
            "name": "C#",
            "level": 70
        }]
    }, {
        "first_name": "Cherna",
        "last_name": "Ninja",
        "age": 100,
        "birth_date": "10/10/2100",
        "birth_place": "Tokyo",
        "gender": "ninja",
        "interests": ["fighting"],
        "avatar": "do-i-exist.png",
        "skills": [{
            "name": "C++",
            "level": 99
        }, {
            "name": "C",
            "level": 99
        }]
    }]
}
        with open('data.json','r') as f:
            json_content = json.load(f)
        self.assertEqual(json_content,data)
    
    def test_business_card_result_files(self):
        expected_files = ['ivo_ivo.html', 'rado_rado.html', 'rosi_rosi.html', 'pavli_pavli.html', 'cherna_ninja.html']
        self.assertEqual(business_card('data.json'),expected_files)

    def test_existance_of_new_files(self):
        os.path.isfile('./ivo_ivo.html')
        os.path.isfile('./rado_rado.html')
        os.path.isfile('./rosi_rosi.html')
        os.path.isfile('./pavli_pavli.html')
        os.path.isfile('./cherna_ninja.html')

if __name__ == '__main__':
    unittest.main()
