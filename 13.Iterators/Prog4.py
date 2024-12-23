class MyNumbers:
  def __init__(self,startValue,endValue):
    self.startValue=startValue
    self.endValue=endValue
  def __iter__(self):
    self.a = startValue
    return self
  def __next__(self):
    if self.a <= endValue:
      startvalue = self.a
      self.a += 10
      return startvalue
    else:
      raise StopIteration

startValue=int(input("Enter Start value"))
endValue=int(input("Enter End value"))

myclass = MyNumbers(startValue,endValue)
myiter = iter(myclass)
for x in myiter:
  print(x)