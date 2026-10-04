
import random
import time

from threading import Thread
from concurrent.futures import ThreadPoolExecutor



class MyThread():
    def __init__(self, id:str ,count_max:int = 1000, sec_wite_time:int = 10):
        super().__init__()
        self.__id = id
        self.__count_max = count_max
        self.__sec_wite_time = sec_wite_time
        
    def run(self, ):
        self.count = 0
        while self.count < self.__count_max + 1:

            print(f'{self.__id} liczy: {self.count}')
            self.count +=1

            wait = random.randint(0, self.__sec_wite_time)
            time.sleep(wait)


if __name__ == '__main__':

    with ThreadPoolExecutor(2) as executor:
        thread_1 = MyThread('A', 100, 1)
        thread_2 = MyThread('B', 10,1)
        executor.submit(thread_1.run)
        executor.submit(thread_2.run)