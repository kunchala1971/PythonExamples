c = 1
def add():
    print(c)
add()

c = 1  # global variable
def add():
    global  c
    c = c + 2  # increment c by 2
    print("TEst " + str(c))

add()

c = 0  # global variable


def add():
    global c
    c = c + 2  # increment by 2
    print("Inside add():", c)

add()

print("In main:", c)
