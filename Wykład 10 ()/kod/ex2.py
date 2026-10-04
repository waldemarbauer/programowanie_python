
import random
import time

from threading import Thread

def run_and_write(id:str ,count_max:int = 1000, sec_wite_time:int = 10):
    count = 0
    while count < count_max + 1:

        print(f'{id} liczy: {count}')
        count +=1

        wait = random.randint(0, sec_wite_time)
        time.sleep(wait)


if __name__ == '__main__':
    # t_list = []
    # for i in range(0,1000):
    #     t_list.append(Thread(target=run_and_write, args=(f'A_{i}', 30, 1)))
    
    # for t in t_list:
    #     t.start()
    
    # for t in t_list:
    #     t.join()
    
    thread_1 = Thread(target=run_and_write, args=('A', 100, 1))
    thread_2 = Thread(target=run_and_write, args=('B', 10,1))
    thread_3 = Thread(target=run_and_write, args=('C', 50,1))
    
    
    thread_1.start()
    thread_2.start()
    thread_3.start()

    thread_1.join()
    thread_2.join()
    thread_3.join()
