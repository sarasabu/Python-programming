import math
a=int(input("Enter the value:"))
s_area=lambda a:a*a
print("Area of square is",s_area(a))
b=int(input("Enter the length:"))
c=int(input("Enter the breadth:"))
r_area=lambda len,ht:len*ht
print("Area of rectangle is",r_area(b,c))
d=int(input("Enter the base:"))
e=int(input("Enter the height:"))
t_area=lambda b,h:1/2*b*h
print("Area of triangle is",t_area(d,e))
