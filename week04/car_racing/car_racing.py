import json
import random

class TypeError(Exception):
    pass

class Car:
    def __init__(self,car,model,max_speed):
            self.car = car
            self.model = model
            self.max_speed = max_speed

    def __str__(self):
        return 'a car {0} with max speed {1}'.format(self.car+' '+self.model,self.max_speed)

class Driver:
    def __init__(self,name,car):
        self.validate_input_params(name,car)

        self.name = name
        self.car = car

    def validate_input_params(self,name,car):
        if type(car) is not Car:
            raise TypeError('Car must be of type <Class> !')

    def __str__(self):
        return '{0} has {1}'.format(self.name,self.car)

class Race:
    def __init__(self,drivers,crash_chance):
        self.validate_input_params(drivers,crash_chance)

        self.drivers = drivers
        self.crash_chance = crash_chance


    def validate_input_params(self,drivers,crash_chance):
        for driver in drivers:
            if type(driver) is not Driver:
                raise TypeError('All drivers must be of class <Driver> !')

    def print(self):
        for driver in self.drivers:
            print(driver)
        print('Crash chance :',self.crash_chance)

    def result(self):
        result = list()
        for index,driver in enumerate(self.drivers):
            crashed = self.crash_chance*random.randint(0,1) - 0.09
            if crashed < 0.3:
                print('Unfortunately {0} has crashed!'.format(driver.name))
                result.append((driver.name,0))
            else:
                result.append((driver.name,1))
        scored = dict()
        score = 8
        for item in result:
            if score > 4:
                if item[1] == 1:
                    scored[item[0]] = score
                    score = score - 2
        print()
        for person in scored:
            print(person,'-',scored[person])
        return scored

class Championship(Race):
    def __init__(self,name,race_count):
        self.name=name
        self.race_count=race_count
        print('Starting a new championship called {0} with {1} races.'.format(self.name,self.race_count))

def top3(filename):
    with open(filename,'r') as json_file:
        data = json.load(json_file)
    winners = dict()
    for race in data['scores']:
        for key,value in race.items():
            if key in winners.keys():
                winners[key] += value
            else:
                winners[key] = value
    winners = sorted(winners.items(),key = lambda x:x[1],reverse=True)
    winners_count = 3
    for index,driver in enumerate(winners):
        name= driver[0]
        score = driver[1]
        if winners_count :
            print(name,'-',score)
            winners_count -= 1

def total_standings(filename):
    print('\nTotal championship standings:')
    with open(filename,'r') as json_file:
        data = json.load(json_file)
    winners = dict()
    for race in data['scores']:
        for key,value in race.items():
            if key in winners.keys():
                winners[key] += value
            else:
                winners[key] = value
    winners = sorted(winners.items(),key = lambda x:x[1],reverse=True) 
    for index,driver in enumerate(winners):
        name= driver[0]
        score = driver[1]
        print(name,'-',score)


