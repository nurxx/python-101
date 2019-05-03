class Singleton(type):
    def __init__(cls, name,bases= None, dictionary= None):
        super().__init__(name,bases,dictionary)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class Hero(metaclass=Singleton):
    def __init__(self,name,title,health):
        self.name = name
        self.title = title 
        self.health = health

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return '{} with health {}'.format(self.title,self.health)

def main():
    hero1 = Hero('Josh Brolin','Thanos',100)
    hero2 = Hero('Tony Stark','Iron Man',0)

    assert hero1 is hero2
    assert id(hero1) == id(hero2)
    assert str(hero1)==str(hero2)
    assert hero1.is_alive() == hero2.is_alive() 

if __name__ == '__main__':
    main()