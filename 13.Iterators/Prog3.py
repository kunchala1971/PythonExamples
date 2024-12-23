class MyNumbers:
    def __init__(self,startValue,inc):
        self.start=startValue
        self.i=inc
    def __iter__(self):
        self.a = self.start
        return self
    def __next__(self):
        x = self.a
        self.a += self.i
        return x
startValue=int(input("Enter any Number It Prints Next 5 Numbers"))
inc=int(input("Enter Increment value"))

myclass = MyNumbers(startValue,inc)

myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
