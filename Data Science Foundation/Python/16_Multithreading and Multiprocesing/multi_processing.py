## process that run in parralll
## CPU-Bound task-task that are heavy on CPU usage(e.g., mathematical computation ,data processing)
## Prallel execution -Multiple cores of the CPU

import multiprocessing
import time
def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"cube: {i*i*i}")

if __name__=="__main__":        

    p1=multiprocessing.Process(target=square_numbers)
    p2=multiprocessing.Process(target=cube_numbers)
    t=time.time()

    ## start hte process
    p1.start()
    p2.start()

    ##wait the process to cmplete
    p1.join()
    p2.join()

    finished_time=time.time()-t
    print(finished_time)
