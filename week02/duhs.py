#duhs.py
import os
import sys

def duhs(path):
    size=0
    for (root, dirs, files) in os.walk(path):
        for file in files:
            current_path = os.path.join(root,file)
            size += os.path.getsize(current_path)
    return float(size/10**9)

def main():
    print(sys.argv[1] + ' size is: ', str(duhs(sys.argv[1]))+'G')

if __name__=='__main__':
    main()