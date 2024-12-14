class MyNumbers:
    def __init__(self,c,inc):
        self.start=c
        self.i=inc
    def __iter__(self):
        self.a = self.start
        return self
    def __next__(self):
        x = self.a
        self.a += self.i
        return x
c=int(input("Enter any Number It Prints Next 5 Numbers"))
inc=int(input("Enter Increment value"))

myclass = MyNumbers(c,inc)

myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
