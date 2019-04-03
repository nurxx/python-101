def elevator_trips(people_weight, people_floors, elevator_floors, max_people, max_weight):
    trips=0
    if len(people_weight) == 0 or len(people_floors) == 0:
        return 0

    while len(people_weight) > 0:
        current_floors=[people_floors[index] for index,person in enumerate(people_weight)
                        if sum(people_weight[:index+1]) <= max_weight and len(people_weight[:index+1]) <= max_people]
        trips+=len(set(current_floors))+1
        people_weight=people_weight[len(current_floors):]
        people_floors=people_floors[len(current_floors):]

    return trips
