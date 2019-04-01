# cat.py
import sys

def cat(arguments):
    my_file=open(arguments)
    lines=my_file.readlines()
    for i in lines:
        print(i.strip('\n'))
    my_file.close()

def main():
    cat(sys.argv[1])

if __name__ == '__main__':
    main()