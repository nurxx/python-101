def elevator_trips(people_weight, people_floors, elevator_floors, max_people, max_weight):
    # person=0
    # current_weight=0
    # current_people=0
    # stops=set()
    # trips=0

    # while person < len(people_weight):
    #     if current_people +1 > max_people or current_weight + people_weight[person] > max_weight:
    #         current_weight= 0
    #         current_people= 0
    #         trips += len(stops)+1
    #         stops.clear()
    #     stops.add(people_floors[person])
    #     current_people += 1
    #     current_weight += people_weight[person]
    #     person+=1
    # return trips + len(stops) + 1

    start=0
    trips =0
    current_weight=0
    current_people=0
    for index,person_weight in enumerate(people_weight):
        current_weight+=person_weight
        if current_weight > max_weight or len(people_weight)==index+1 or current_people==max_people:
            trips+=len(set(people_floors[start:index]))+1
            current_weight=person_weight
            start=index
            current_people=0
        current_people+=1

    #trips+=len(set(people_floors[start:index]))+1
    return trips