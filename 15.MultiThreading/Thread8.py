from threading import *
import time
def display():
    print("\n"+ current_thread().name,"...started\n")
    time.sleep(1)
    print("\n"+ current_thread().name,"...ended\n")

t1=Thread(target=display,name="ChildThread1")
t2=Thread(target=display,name="ChildThread2")
t3=Thread(target=display,name="ChildThread3")
t1.start()
t2.start()
t3.start()
l=enumerate()# it returns  current live threads list
for t in l:
    print("\nStart Thread Name:",t.name)
    time.sleep(1)
l=enumerate()
print("\nAfter Completeion of First Enumerate")
for t in l:
    print("\nThread Name:",t.name)
