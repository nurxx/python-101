import csv
def find_index(item, filter_keys):
    for index,elem in enumerate(filter_keys):
        if elem == item:
            return index

def filter(file_name, **kwargs):
    result = []
    with open(file_name,'r') as csv_file:
        data = csv.reader(csv_file)
        filters = kwargs
        filter_keys = ['full_name','favourite_color','company_name','email','phone_number','salary']
        for row in data:
            print(row)
            all_constraints = 0
            for key,value in filters.items():
                if key.endswith('__startswith'):
                    item = key.replace('__startswith','')
                    idx = find_index(item ,filter_keys)
                    if row[idx].startswith(value):
                        all_constraints += 1
                if key.endswith('__contains'):
                    item = key.replace('__contains','')
                    idx = find_index(item ,filter_keys)
                    if value in row[idx]:
                        all_constraints+=1
                if key.endswith('__gt'):
                    item = key.replace('__gt','')
                    idx = find_index(item ,filter_keys)
                    if int(row[idx]) > int(value): 
                        all_constraints += 1
                if key.endswith('__lt'):
                    item = key.replace('__lt','')
                    print(key)
                    idx = find_index(item ,filter_keys)
                    if int(row[idx]) < int(value): 
                        all_constraints += 1
                else:
                    if key != 'order_by':
                        idx = find_index(key,filter_keys)
                        if value == row[idx]:
                            all_constraints += 1
                    else:
                        idx = find_index(value,filter_keys)
                        result = sorted(result,key=lambda x:x[idx])
            if all_constraints == len(filters):
                result += [row]

    return result

def main():
    output = filter('example_data.csv',email__startswith = 'ng')
    for row in output:
        print(' '.join(row))

if __name__ =='__main__':
    main()