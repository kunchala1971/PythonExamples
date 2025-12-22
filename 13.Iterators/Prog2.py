#Iter with Class
class MyNumbers:
  def __iter__(self):
    self.count = 0
    self.increment = input("Enter Increment Value")
    return self
  def __next__(self):
    value= self.count
    self.count += int(self.increment)
    return value

myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
