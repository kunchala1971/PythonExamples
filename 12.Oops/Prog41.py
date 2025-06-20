"""
The Relation between parent class and child class is called inheritance
or
The mechanisam between Base Class and Derived class is called inheritance
"""
#Single Inheritance
class Parent(object):
    def __init__(self, pname):
        self.pname = pname
    def get_details(self):
        return self.pname
class Child(Parent):
    def __init__(self, pname, name, branch, year):
        Parent.__init__(self, pname)
        self.name=name
        self.branch = branch
        self.year = year
    def insertData(self,pname,name,branch,year):
        Parent.__init__(self, pname)
        self.name=name
        self.branch=branch
        self.year=year
    def get_details(self):
        #returns a string containing student's details
        return "Parent Name is %s Child name is %s studies %s and is in %s year." \
               % (self.pname,self.name, self.branch, self.year)

fathername=input("Enter Father Name")
studentname=input("Enter student Name")
branch=input("Enter Branch Code")
joinyear=input("Enter Join Year")
child=Child(fathername,studentname,branch,joinyear)
print(child.get_details())
child.insertData('KSR','Venkat','B.Tech',2022)
print(child.get_details())

