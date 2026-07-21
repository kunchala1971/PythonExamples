#Parameterised  constructor
class Student:
    def __init__(self,code,name,course): #parameterised
        self.code=code
        self.name=name
        self.course=course
    def setStudentData(self,code,name,course):
        self.code = code
        self.name = name
        self.course = course
    def showStudentData(self):
        print("Code:",self.code)
        print("Name:",self.name)
        print("Course:",self.course)

# parameterised constructor
code=int(input("Enter Code"))
name=input("Enter Name")
course=input("Enter Course")
sri=Student(code,name,course)
sri.showStudentData()

code=int(input("Enter Code"))
name=input("Enter Name")
course=input("Enter Course")
sri.setStudentData(code,name,course)
sri.showStudentData()

