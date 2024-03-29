import time
from random import randint
import _thread

def main():
    while True:
        print("I'm printing on thread:")
        print(_thread.get_ident())
        time.sleep(randint(1,3))
    return

def print_func():
    while True:
        print("I'm printing on thread:")
        print(_thread.get_ident())
        time.sleep(randint(3,6))
    return