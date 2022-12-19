class Student:
    "information about the class"
    studentcount=0
    def __init__(self,roll,name,course):
        self.roll=roll
        self.name=name
        self.course=course
        Student.studentcount=Student.studentcount+1
    def displaycount():
        print("no:of student objects",student.studentcount)
    def display(self):
        print("Roll No=",self.roll)
        print("name=",self.name)
        print("coursename=",self.course)
list=[]
list.append(Student(31,'Anu','MCA'))
list.append(Student(35,'Sruti','B Tech'))
list.append(Student(48,'Jeevan','MCA'))
for obj in list:
    print(obj.roll,obj.name,obj.course,sep=' ')
