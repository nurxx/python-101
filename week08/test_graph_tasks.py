import unittest
from deep_find_all import *
from deep_update import *

class TestGraphTasks(unittest.TestCase):
    def setUp(self):
        self.data1 =  {
                    'a':5,
                    'b':4,
                    'c':{
                    'd':'4',
                    11:11,
                    'v':{
                        'panda1':'hi'
                    }
                    },
                    'panda':[
                    {
                    'panda2':'hello'
                    }
                    ]
                }
        self.data2 = {
            'a':5,
            'b':4,
            'c':{
            'd':'4',
            11:11,
            'v':{
                'panda1':'hi',
                'panda2':'foo'
            }
            },
            'panda':[
            {
            'panda2':'hello'
            }
            ]
        }

    def test_deep_find_all_values_of_a_certain_key_in_data(self):
        expected_output = ['foo','hello']
        self.assertTrue(deep_find_all_dfs(self.data2,'panda2'),expected_output)

    def test_when_update_all_occurences_of_key_with_certain_value(self):
        to_be_updated = self.data2
        expected_output ={
                        'a':5,
                        'b':4,
                        'c':{
                        'd':'4',
                        11:11,
                        'v':{
                            'panda1':'hi',
                            'panda2':'Hello I am HackPanda'
                        }
                        },
                        'panda':[
                        {
                        'panda2':'Hello I am HackPanda'
                        }
                        ]
                    }
        self.assertEqual(deep_update(to_be_updated,'panda2','Hello I am HackPanda'),expected_output)

if __name__ == '__main__':
    unittest.main()