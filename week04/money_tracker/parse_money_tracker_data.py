class Parser:
    @classmethod
    def find(cls,llist,date):
        for index,item in enumerate(llist):
            if date in item:
                return index

    @classmethod
    def parse_money_tracker_data(cls,file_name):
        with open(file_name,'r') as file:
            content = file.readlines() 

        data = list()
        for line in content:
            if line.startswith('==='):
                date = line
                data += [[date]]
            else:
                data[cls.find(data,date)] += [line]

        return data




