class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
       
    def area(self):
        return (self.length*self.width)
   
    
   
l=int(input("Enter the length of 1st Rectangle: "))
w=int(input("Enter the width of 1st rectangle: "))
l2=int(input("Enter the length of 2nd Rectangle: "))
w2=int(input("Enter the width of 2nd rectangle: "))

r1= Rectangle(l,w)
r2= Rectangle(l2,w2)

print ("\nArea of 1st Rectangle : ", r1.area())
print ("\nArea of 2nd Rectangle : ", r2.area())
x=r1.area()
y=r2.area()
if(x>y):
    print("1st Rectangle is bigger")
elif(x==y):
    print("Both rectangles are equal")
else:
    print("2nd rectangle is bigger")
    
