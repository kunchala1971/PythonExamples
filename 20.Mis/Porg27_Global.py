c = 1
def add():
    print(c)
add()

def add():
    global  c
    c = c + 2  # increment c by 2
    print("Test " + str(c))

add()

def add():
    global c
    c = c + 5  # increment by 2
    print("Inside add():", c)

add()

print("In main:", c)
