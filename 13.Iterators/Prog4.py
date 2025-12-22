class MyNumbers:
  def __init__(self,startValue,endValue,inc):
    self.startValue=startValue
    self.endValue=endValue
    self.inc=inc
  def __iter__(self):
    self.a = startValue
    return self
  def __next__(self):
    if self.a <= endValue:
      startvalue = self.a
      self.a += self.inc
      return startvalue
    else:
      raise StopIteration

startValue=int(input("Enter Start value"))
endValue=int(input("Enter End value"))
inc=int(input("Enter Increment Value"))

myclass = MyNumbers(startValue,endValue,inc)
myiter = iter(myclass)
# for x in myiter:
#   print(x)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))