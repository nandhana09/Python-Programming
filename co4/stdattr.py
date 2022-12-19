class Student:
    "information about the class"
    studentcount=0
    def __init__(self,roll,name,course):
        self.roll=roll
        self.name=name
        self.course=course
        Student.studentcount=Student.studentcount+1
    def displaycount():
        print("No:of student objects",Student.studentcount)
    def display(self):
        print("Roll No=",self.roll)
        print("name=",self.name)
        print("course name=",self.course)
    def __del__(self):
        class_name=self._class_._name_
        print(class_name,"destroyed")
        s1=Student(501,"Abhijith","MCA")
        s2=Student(503,"Ajmi","MCA")
        print(getattr(s1,'name'))
        print(hasattr(s2,'name'))
        setattr(s1,'height',152)
        print(getattr(s1,'height'))
        delattr(s1,'course')
        print(hasattr(s2,'course'))
        setattr(s1,'course','Btech')
        s1.display()
