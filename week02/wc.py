#wc.py
import sys

def wc(command,filename):
    my_file=open(filename)
    if command == 'chars':
        output = len(''.join(my_file.readlines()))
    elif command == 'words':
        output=len((''.join(my_file.readlines())).split())
    elif command == 'lines':
        output = len(my_file.readlines())
    my_file.close()

    return output

def main():
    print(wc(sys.argv[1],sys.argv[2]))

if __name__=='__main__':
    main()