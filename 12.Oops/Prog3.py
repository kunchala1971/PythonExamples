#What is the constructor
#to initialize the class members
#using __init__ method (it provides system(pre-defined method))
#whenever we instantiated the class automatically constructor should be executed
#defalut constructor
class Student:
    def __init__(self):#default constructor
        self.code=100
        self.name="Venkat"
        self.course="Python"
    def setStudentData(self,code,name,course):
        self.code = code
        self.name = name
        self.course = course
    def showStudentData(self):
        print("Code:",self.code)
        print("Name:",self.name)
        print("Course:",self.course)
#when ever the class is instantiated
#automatically the constructor should be execute

sri=Student()
sri.showStudentData()
code=int(input("Enter Code"))
name=input("Enter Name")
course=input("Enter Course")
sri.setStudentData(code,name,course)
sri.showStudentData()