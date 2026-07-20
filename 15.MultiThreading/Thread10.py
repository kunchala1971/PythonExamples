from threading import *
import time
def display():
    for i in range(10):
        print("\nSeetha Thread " + str(i))
        time.sleep(2)
t=Thread(target=display)
t.start()
#t.join()#This Line executed by Main Thread
t.join(6)#This Line executed by Main Thread after certain period
for i in range(10):
    print("Rama Thread")
