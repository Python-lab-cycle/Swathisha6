from graphics.rectangle import*
from graphics.circle import*
from graphics.dgraphics.cuboid import*
from graphics.dgraphics.sphere import*
num1=int(input("enter the length of rectangle"))
num2=int(input("enter the breadth of recxtangle"))
print("area=", RArea(num1, num2))
print("perimeter=", Rperimeter(num1, num2))


radius=int(input("enter the rtadius of circle"))
print("circle area", CArea(radius))
print("circle area", CPerimeter(radius))


radius=int(input("enter the rtadius of sphere"))
print("sphere area", Asphere(radius))
print("perimeter of sphere", Psphere(radius))


edge=int(input("enter the edge of cuboid"))
l=int(input("enter the length of cuboid"))
b=int(input("enter the breadth of cuboid"))
h=int(input("enter the height of cuboid"))
print("area of cuboid", Acuboid(radius))
print("perimeter of cuboid", Pcuboid(l,b,h))
