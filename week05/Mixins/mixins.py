import json

from dicttoxml import *
from xmltodict import *

class Jsonable:
    def to_json(self,indent = 4,**kwargs):
        dictionary = self.__dict__
        class_type = self.__class__.__name__
        json_dict = dict()
        json_dict['type'] = class_type
        json_dict['dict'] = dictionary

        return json.dumps(json_dict,indent=indent)

    @classmethod
    def from_json(cls,json_string):
        data = json.loads(json_string)
        kwargs = data['dict']
        return cls(**kwargs)

class Xmlable:
    def to_xml(self,**kwargs):
        dictionary = self.__dict__
        class_type = self.__class__.__name__

        return dicttoxml(class_type,dictionary)

    @classmethod
    def from_xml(cls,xml_string):
        attributes =  xmltodict(xml_string)
        return cls(**attributes)

class Panda(Jsonable,Xmlable):
    def __init__(self,**kwargs):
        for key,value in kwargs.items():
            setattr(self,key,str(value))

    def __eq__(self,other):
        return self.__dict__.items()==other.__dict__.items()

class Kangaroo(Jsonable,Xmlable):
    def __init__(self,**kwargs):
        for key,value in kwargs.items():
            setattr(self,key,str(value))

    def __eq__(self,other):
        return self.__dict__.items() == other.__dict__.items()

class Flamingo(Jsonable,Xmlable):
    def __init__(self,**kwargs):
        for key,value in kwargs.items():
            setattr(self,key,str(value))

    def __eq__(self,other):
        return len(self.__dict__.items()&other.__dict__.items()) == len(self.__dict__)

if __name__== '__main__':
    panda = Panda(name='HackPanda',weight=90,food='code',hobby='sleeping',color='black and white')
    json_string = panda.to_json(0)
    xml_string = panda.to_xml()
    assert Panda.from_json(json_string) == Panda.from_xml(xml_string)