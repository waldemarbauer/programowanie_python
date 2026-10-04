from threading import Thread
from concurrent.futures import ThreadPoolExecutor
import time
import random

variable: int = 1
FILENAME: str = 'test'


def read_from_file() -> int:
    with open(FILENAME, 'r+') as file:
        val = file.read()
        return int(val)


def write_to_file(val: int) -> None:
    with open(FILENAME, 'w') as file:
        file.write(str(val))


def increment_value_in_file():
    value = read_from_file()
    write_to_file(value + 1)

if __name__ == '__main__':

    write_to_file(0)


    with ThreadPoolExecutor(10) as executor:
        for _ in range(10):
            executor.submit(increment_value_in_file)

    print("Final value: ", read_from_file())