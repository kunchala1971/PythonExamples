#Hirarchical Inheritance
class Person(object):
    def __init__(self, name,dept):
        self.name = name
        self.dept = dept
    def get_details(self):
        return self.name+ "-"+self.dept
class Student(Person):
    def __init__(self, name,dept,branch, year):
        Person.__init__(self, name,dept)
        self.branch = branch
        self.year = year
    def get_details(self):
        return "%s Department %s studies %s and is in %s year." \
               % (self.dept,self.name, self.branch, self.year)
class Teacher(Person):
    def __init__(self, name,dept,papers):
        Person.__init__(self, name,dept)
        self.papers = papers
    def get_details(self):
        return "%s Deptartment %s teaches %s" % \
               (self.dept,self.name, ','.join(self.papers))
    def get_papers(self):
        return self.papers

student = Student('Niharika',"Eelectronics", 'ECE', 2017)
teacher = Teacher('Venkat',"Computers", ['C', 'C++','java','Python'])
print(student.get_details())
print(teacher.get_details())
print(teacher.get_papers())
