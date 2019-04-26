import sys
from car_racing import *

def main():
    with open('cars.json','r') as json_file:
        data = json.load(json_file)

    drivers = list()

    for person in data['people']:
        car = Car(person['car'],person['model'],person['max_speed'])
        driver = Driver(person['name'],car)
        drivers.append(driver)


    if sys.argv[1] == 'start':
        races=[]
        championship= Championship(sys.argv[2],sys.argv[3])

        for i in range(1,int(sys.argv[3])+1):
            print('\nRace {0}'.format(str(i)))
            print('##### START #####')
            crash_chance = random.uniform(0,1)
            race = Race(drivers,crash_chance)
            races.append(race.result())

        result = dict()
        result['scores']=races
        with open('result.json','w') as json_file:
            json.dump(result,json_file,indent=4)
        total_standings('result.json')
    elif sys.argv[1] =='standings':
        top3('result.json')

if __name__ == '__main__':
    main()