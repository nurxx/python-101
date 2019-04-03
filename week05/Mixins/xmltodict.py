def xmltodict(xml_string):
    xml_string = xml_string.replace('<','')
    xml_string = xml_string.replace('>','#')
    xml_string = xml_string.replace('/','#')

    llist_elems = xml_string.split('#')
    llist_elems = llist_elems[:-1]
    llist_elems = llist_elems[1:]

    tags = list()
    values = list()

    for index,elem in enumerate(llist_elems):
        if llist_elems.count(elem) == 2:
            if elem not in tags:
                tags.append(elem)
        else:
            values.append(elem)

    dictionary = dict(zip(tags,values))
    return dictionary