class Student:
    "information about the class"
    studentcount=0
    def __init__(self,roll,name,course):
        self.roll=roll
        self.name=name
        self.course=course
        Student.studentcount=Student.studentcount+1
    def displaycount():
        print("no:of student objects",Student.studentcount)
    def display(self):
        print("Roll No=",self.roll)
        print("name=",self.name)
        print("coursename=",self.course)
    def __del__(self):
        class_name=self.__class__.__name__
        print(class_name,"destroyed")
    s1=Student(501,"Abhijith","MCA")
    s2=Student(503,"Ajmal","MCA")
    print(getattr(s1,'name'))
    s1.display()
    s2.display()
    Student.displaycount()
    del s1
        
