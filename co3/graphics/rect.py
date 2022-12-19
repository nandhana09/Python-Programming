class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def display(self):
        print ("Length of Rectangle is: ", self.length)
        print ("Breadth of Rectangle is: ", self.breadth)
    def area(self):
        return (self.length*self.breadth)
    def perimeter(self):
        return (2*self.length + 2*self.breadth)
   
l = int (input("Enter the length of the Rectangle: "))
b = int (input("Enter the breadth of rectangle: "))

r1 = Rectangle(l , b)
print ("Rectangle object details are:")
r1.display()
print("")
print ("Area of Rectangle is: ", r1.area())
print("")
print ("The Perimeter of the Rectangle is: ", r1.perimeter())

