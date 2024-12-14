#Single try multiple Exceptions
cnames="Srinviasa"
try:
  print(cnames + str(4545))
except NameError:
  print("Variable name is not defined")
except:
  print("Something else went wrong")
else:
  print("Program Running is Over")