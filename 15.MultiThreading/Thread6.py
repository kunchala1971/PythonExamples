#show the threads identity
from threading import *
def test():
    print("Child Thread")
t=Thread(target=test)
t.start()
print("Main Thread Identification Number:",current_thread().ident)
print("Child Thread Identification Number:",t.ident)
