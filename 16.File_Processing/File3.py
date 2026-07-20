#file is existed then append otherwise create
try:
  filename=input("enter file name")
  f = open(filename, "x")
  print("Your Try Block")
except:
  print("Your in Exception Block")
  f = open(filename,"a")
finally:
  content=input("enter content")
  f.write("\n"+content)
  f=open(filename)
  print(f.read())
  f.close()
