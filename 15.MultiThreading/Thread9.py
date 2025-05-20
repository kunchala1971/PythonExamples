from threading import *
import time
def display():
    print(current_thread().name,"...started\n")
    time.sleep(3)
    print(current_thread().name,"...ended\n")

t1=Thread(target=display,name="ChildThread1")
t2=Thread(target=display,name="ChildThread2")

t1.start()
t2.start()

print(t1.name,"is Alive :",t1.is_alive())
print(t2.name,"is Alive :",t2.is_alive())
time.sleep(4)
print(t1.name,"is Alive :",t1.is_alive())
print(t2.name,"is Alive :",t2.is_alive())
