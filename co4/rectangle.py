class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
       
    def area(self):
        return (self.length*self.breadth)
   
    def perimeter(self):
        return (2*self.length + 2*self.breadth)
   
l=int(input("Enter the length of 1st Rectangle: "))
b=int(input("Enter the breadth of 1st rectangle: "))
l2=int(input("Enter the length of 2nd Rectangle: "))
b2=int(input("Enter the breadth of 2nd rectangle: "))

r1= Rectangle(l,b)
r2= Rectangle(l2,b2)

print ("\nArea of 1st Rectangle : ", r1.area())
print ("\nArea of 2nd Rectangle : ", r2.area())
print ("\nPerimeter of 1st Rectangle : ", r1.perimeter())
print ("\nPerimeter of 2nd Rectangle : ", r2.perimeter())
x=r1.area()
y=r2.area()
if(x>y):
    print("1st Rectangle is bigger")
elif(x==y):
    print("Both rectangles are equal")
else:
    print("2nd rectangle is bigger")
    
