def birthday_ranges(birthdays, ranges):
    dictionary=dict()
    for dates in ranges:
        dictionary[dates]=0

    for bday in birthdays:
        for r in ranges:
            if bday>=r[0] and bday<=r[1]:
                dictionary[r]+=1

    return list(dictionary.values())