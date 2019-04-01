# cat2.py
import sys
from cat import *
def cat2(arguments):
    for argument in arguments:
        cat(argument)
        print()

def main():
    cat2(sys.argv[1:])

if __name__ == '__main__':
    main()
