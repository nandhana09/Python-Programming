square=lambda x:x*x
x=int(input("Enter a side"))
print("the area of square is",square(x))
rect=lambda l,b:l*b
l=int(input("Enter the length"))
b=int(input("Enter the breadth"))
print("the area of rectangle is",rect(l,b))
h=int(input("Enter height"))
d=int(input("Enter breadth"))
z=lambda h,d:0.5*h*d
print("Area of triangle:",z(h,d))
