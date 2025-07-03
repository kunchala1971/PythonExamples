#Multilevel Inheritance
class GrandParent(object):
    def __init__(self, gname):
        self.gname = gname
    def get_details(self):
        return self.gname

class Parent(GrandParent):
    def __init__(self, pname,gname):
        GrandParent.__init__(self, gname)
        self.pname = pname
    def get_details(self):
        return self.pname

class Child(Parent):
    def __init__(self,gname, pname,name, branch, year):
        Parent.__init__(self, pname,gname)
        self.name=name
        self.branch = branch
        self.year = year
    def get_details(self):
        "Returns a string containing student's details."
        return "Grand Father Name is %s and Parent Name is %s " \
               "Chid name is %s studies %s and " \
               "is in %s year." \
               % (self.gname,self.pname,self.name,
                  self.branch, self.year)
        # print("Grand Father Name is %s and Parent Name is %s " \
        #        "Chid name is %s studies %s and " \
        #        "is in %s year." \
        #     % (self.gname, self.pname, self.name,
        #        self.branch, self.year))

gpname=input("Enter Grand Parent Name")
pname=input("Enter  Parent Name")
cname=input("Enter Child Name")
course=input("Enter Course Name")
jyear=input("Enter Join Year")
Child1 = Child(gpname,pname,cname,course,jyear)
print(Child1.get_details())
# Child1.get_details()