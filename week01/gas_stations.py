def gas_stations(distance, tank_size, stations):
    gas_stations_in_route = []
    distance_travelled = 0
    while True:
        if distance_travelled + tank_size >= distance:
            break
        gas_station=max([station for station in stations if station <= distance_travelled + tank_size])
        gas_stations_in_route.append(gas_station)
        distance_travelled = gas_station

    return gas_stations_in_route

