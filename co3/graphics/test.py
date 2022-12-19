from circle import *
from rectangle import*

r=int(input("Enter radius of circle"))
l=int(input("Enter length of rectangle"))
b=int(input("Enter breadth of rectangle"))
print("Area of circle:",circle(r))
print("Perimeter of circle:",perimeter(r))
print("Area of rectangle",rectangle(l,b))
print("Perimeter of rectangle",peri(l,b))
from threeDgraphics import sphere
from threeDgraphics import cuboid
r1=int(input("Enter radius of sphere"))
l1=int(input("Enter the length of cuboid"))
h1=int(input("Enter the height of cuboid"))
w1=int(input("Enter the width of cuboid"))
print("Area of sphere:",sphere.sphere(r1))
print("Area of cuboid:",cuboid.cuboid(l1,h1,w1))
print("Perimeter of cuboid:",cuboid.peri(l1,h1,w1))

