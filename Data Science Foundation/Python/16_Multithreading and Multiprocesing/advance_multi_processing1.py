## Multiprocessing With Process Pool executor

from concurrent.futures import ProcessPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"Number :{number* number}"

numbers=[1,2,8,4,5]
if __name__=="__main__":

    with ProcessPoolExecutor(max_workers=4) as executor:
        results=executor.map(print_number,numbers)

    for result in results:
        print(result)    