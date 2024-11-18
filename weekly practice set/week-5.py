#q1
x = int(input("Enter x"))
y = int(input("Enter y"))
z = int(input("Enter z"))
if(x==0):
    print(y+z)
elif(x==1):
    print(y-z)
elif(x==2):
    print(y*z)
elif(x==3):
    print(y/z)
else:
    print("Invalid Input")


#q2
a = int(input("Enter a"))
b = int(input("Enter b"))
c = int(input("Enter c"))
if(a**2==(b**2)+(c**2)):
    print("A IS 90")
else:
    print("A IS NOT 90")



#q3
m = int(input("Enter your marks"))
if m>=90:
    print("E")
elif 80<=m<90 :
    print("A")
elif 70<=m<80:
    print("B")
elif 60<=m<70:
    print("C")
elif 50<=m<60:
    print("D")
elif 35<=m<50:
    print("P")
else:
    print("F")



#q4
x = int(input("Enter x"))
y=0
if(x==6):
    y=x+10
elif(x==7):
    y=x*x
elif(x==12):
    y=2*x+4
else:
    y=x*6-1

print(y)


#q5
from math import sqrt
d = int(input("Enter a"))
e = int(input("Enter b"))
f = int(input("Enter c"))
x = -1*(d/2)
y = -1*(e/2)
r = sqrt((d**2)/4+(e**2)/4-f)
print(f"center is {x},{y}")
print(f"Radius is {r}")

