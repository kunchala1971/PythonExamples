#Constructor Example
class MyClass:
    def __init__(self,code,name):
        self.code=code
        self.name=name
    def insertData(self,code,name):
        self.code = code
        self.name = name
    def showData(self):
        print("Code :",self.code)
        print("Name:",self.name)
code=input("Enter code")
name=input("Enter Name")
#when the class is instantiated then init method is executed
p=MyClass(code,name)#Construct the class init functions
p.showData()
p.insertData(101,"Kishore")
p.showData()

