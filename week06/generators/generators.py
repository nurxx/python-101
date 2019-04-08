import os 

def chain(*args):
    index = 0
    while index != len(args):
        for arg in args[index]:
             yield arg
        index += 1

def compress(iterable,mask):
    compressed = zip(iterable,mask)
    for item in compressed:
        if item[1] == True:
            yield item[0]


def cycle(iterable):
    index = 0
    while index == 0:
        for arg in iterable:
            yield arg

def book_reader(directory):
    for file in sorted(os.listdir('./{}'.format(directory))):
        print(file)
        with open('{}/'.format(directory)+file,'r') as f:
            lines = f.readlines()
            for index,line in enumerate(lines):
                if line.startswith('#'):
                    yield line





# endless = cycle(range(0,10))
# for item in endless:
#     print(item)

print(book_reader('Book'))