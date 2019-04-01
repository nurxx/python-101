#sum_numbers.py
import sys 

def sum_numbers(filename):
    the_sum=0
    my_file=open(filename)
    lines=my_file.readlines()
    for line in lines:
        line=line.strip('\n')
        the_sum+=sum(list(map(int,line)))
    my_file.close()
    return the_sum


def main():
    print(sum_numbers(sys.argv[1]))

if __name__=='__main__':
    main()
