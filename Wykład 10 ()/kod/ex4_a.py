
import random
import time

from concurrent.futures import ThreadPoolExecutor



def run_and_write(id:str ,count_max:int = 1000, sec_wite_time:int = 10):
    count = 0
    while count < count_max + 1:

        print(f'{id} liczy: {count}')
        count +=1

        wait = random.randint(0, sec_wite_time)
        time.sleep(wait)


if __name__ == '__main__':

    with ThreadPoolExecutor(2) as executor:
        executor.submit(run_and_write , 'A', 100, 1)
        executor.submit(run_and_write, 'B', 10,1)