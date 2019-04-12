import time
import datetime

class performance:
    def __init__(self,file_name):
        self.file_name = file_name

    def __enter__(self):
        self.time = datetime.datetime.now()
        self.start_program = time.time()

        return self

    def __exit__(self,*args):
        self.end_program = time.time()
        self.execution_time = self.end_program - self.start_program
        self.file = open(self.file_name,'a')
        self.file.write('Date {0}. Execution time {1}.\n'.format(self.time,self.execution_time))
        self.file.close()


def get_low():
    time.sleep(2)
    return 'Get low'

with performance('performance.txt'):
    get_low()


