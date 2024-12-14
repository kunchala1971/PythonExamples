#file is existed then append other wise create
try:
  filename=input("enter file name")
  f = open(filename, "x")
except:
  f = open(filename,"a")
finally:
  content=input("enter content")
  f.write("\n"+content)
  f=open(filename)
  print(f.read())
  f.close()
