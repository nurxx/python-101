# generate_numbers.py
import sys
from random import randint


def generate_numbers(filename, numbers):
    my_file=open(filename,'w+')
    for i in range(int(numbers)):
        my_file.write(str(randint(1,1000))+' ')
    my_file.close()


def main():
    generate_numbers(sys.argv[1],sys.argv[2])

if __name__ == '__main__':
    main()