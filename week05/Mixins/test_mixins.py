import unittest
from mixins import *

class TestMixins(unittest.TestCase):
    def test_when_parsing_object_to_json(self):
        expected_json_string = """{
"type": "Panda",
"dict": {
"name": "HackPanda",
"weight": "123.2",
"food": "code"
}
}"""
        panda = Panda(name='HackPanda',weight=123.2,food='code')
        self.assertEqual(panda.to_json(0),expected_json_string)

    def test_when_parsing_from_json_to_object(self):
        json_string= '{"type": "Flamingo", "dict": {"name": "Flamingo1","weight": "42.1","height":"148", "is_mammal": false}}'
        self.assertEqual(Flamingo(name='Flamingo1',weight=42.1,height=148,is_mammal=False),Flamingo.from_json(json_string))

    def test_when_parsing_object_to_xml(self):
        kangaroo = Kangaroo(name='PyPy',weight=126.2,jump=True,color='Desert Sand')
        expected_xml_string = '<Kangaroo><name>PyPy</name><weight>126.2</weight><jump>True</jump><color>Desert Sand</color></Kangaroo>'
        self.assertEqual(kangaroo.to_xml(),expected_xml_string)

    def test_when_parsing_from_xml_to_object(self):
        kangaroo = Kangaroo(name='PyPy',weight=126.2,jump=True,color='Desert Sand')
        xml_string = '<Kangaroo><name>PyPy</name><weight>126.2</weight><jump>True</jump><color>Desert Sand</color></Kangaroo>'
        self.assertEqual(Kangaroo.from_xml(xml_string),kangaroo)

    def test_result_when_parsing_xml_and_json_string_with_same_result_object(self):
        panda = Panda(name='HackPanda',weight=90,food='code',hobby='sleeping',color='black and white')
        json_string = panda.to_json(0)
        xml_string = panda.to_xml()
        self.assertTrue(Panda.from_json(json_string),Panda.from_xml(xml_string))

if __name__=='__main__':
    unittest.main()
