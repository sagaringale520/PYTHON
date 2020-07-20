#Java Program to Find all Roots of a Quadratic Equation
from math import sqrt

a=1;
b=-1;
c=-6;

base=(b*b)-4*a*c

rBase=sqrt(int(base))

r1=(-b-rBase)/2*a

r2=(-b+rBase)/2*a

print(int(r1))
print(int(r2))