class Student:
    def __init__(self,roll,name,course):
        self.roll=roll
        self.name=name
        self.course=course
    def display(self):
        print("Roll No=",self.roll)
        print("name=",self.name)
        print("course name=",self.course)
class Mark:
    def __init__(self,mark):
        self.mark=mark
class Details(Student,Mark):
    def __init__(self,mark):
        self.hostelflag=hostelflag
    def displayDetails(self):
        self.display()
        print("marks=",self.mark)
        print("marks=",self.hostelflag)
s1=Details(501,"Nandhu","MCA",80,False)
s1.displayDetails()
    
