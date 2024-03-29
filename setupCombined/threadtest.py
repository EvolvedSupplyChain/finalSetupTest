import machine
import _thread
import time
from random import randint
import threadimptest

led = machine.Pin("LED", machine.Pin.OUT)


def blink_func():
    while True:
        led.toggle()
        print("I'm blinking on thread:")
        print(_thread.get_ident())
        time.sleep(randint(1,4))
    
    
def print_func():
    while True:
        print("I'm printing on thread:")
        print(_thread.get_ident())
        time.sleep(randint(3,6))
    

def import_test():
    import threadimptest
    threadimptest.main()
#_thread.start_new_thread(blink_func,())
#_thread.start_new_thread(print_func,())

#blink_func()
time.sleep(3)
_thread.start_new_thread(threadimptest.print_func,())
#_thread.start_new_thread(import_test,())
#print_func()
time.sleep(2)
blink_func()