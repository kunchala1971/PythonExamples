#global variable
def foo():
    x = 20
    def bar():
        global x
        x = 25
        print("After calling bar: ", x)
    def myfun():
        global x
        x = 30
        print("After calling MyFun: ", x)
    def subfun():
        global x
        x = x + 45
        print("After calling SubFun: ", x)
    print("Before calling bar: ", x)#20
    print("Calling bar now")
    bar()#25
    print("Calling subfun now")
    myfun() #30
    subfun() #75

foo()
print("x in main : ", x)
#out side funtion anywhere we can define the global


