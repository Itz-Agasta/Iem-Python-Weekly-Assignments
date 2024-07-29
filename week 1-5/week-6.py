#q1
import numpy as np

a = int(input("Enter a"))
b = int(input("Enter b"))
c = int(input("Enter c"))

p = int(input("Enter p"))
q = int(input("Enter q"))
r = int(input("Enter r"))

A = np.array([[a,b],[p,q]])
B = np.array([-c,-r])

if(np.linalg.det(A)==0):
   print("Lines are parallel")
else:
   ans = np.linalg.solve(A,B)
   print(f"Point of intersection is {ans[0]},{ans[1]}")


#q2
from math import acos
from math import degrees

a = int(input("enter a"))
b = int(input("enter b"))
c = int(input("enter c"))
ans = ((a**2) - (b**2) - (c**2))/(-2*b*c)
A = degrees(acos(ans))
print(A)



#q3
from math import sqrt

a = int(input('enter a '))
b = int(input('enter b '))
c = int(input('enter c '))
d = int(input('enter d '))
e = int(input('enter e '))

ans = (a*c + b*d + e)/sqrt(c**2 + d**2)
print(ans)



#q4
import math
import cmath

a = int(input('enter a '))
b = int(input('enter b '))
c = int(input('enter c '))
d = b**2 - 4*a*c

if d>0:
    x1 = (-b + math.sqrt(d))/2*a
    x2 = (-b - math.sqrt(d))/2*a
    print(x1,x2)

elif d==0:
    x = -b/2*a
    print(x)

else:
    x1 = (-b + cmath.sqrt(d))/2*a
    x2 = (-b + cmath.sqrt(d))/2*a
    print(x1,x2)



#q5
a = int(input("enter a "))
b = int(input("enter b "))
c = int(input("Enter c "))
if b==0:
    print("Vertical line")
else:
    m = -(a/b)
    print(m)

