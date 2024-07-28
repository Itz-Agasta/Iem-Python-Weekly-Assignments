#q1
c = input("Enter a character: ")
c=c.upper()
l=len(c)
if(l>1):
    print("Invalid")

else:
    if 65<=ord(c)<=90 :
        if c in ['A','E','I','O','U']:
            print("Vowel")

        else:
            print("Consonant")

    else:
        print("Not a letter")



#q2

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
max = 0;
for i in [a,b,c]:
    if(i>max):
        max=i

print("Maximum is ",max)



#q3

a = int(input("Enter your age:"))
if(a>=18):
    print("You are eligible to vote")
else:
    print("Not eligible to vote")



#q4

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
min = 999999999999;
for i in [a,b,c]:
    if(i<min):
        min=i

print("Minimum is ",min)



#q5

import math
r = float(input("Enter radius: "))
h = float(input("Enter height"))
a = (1/3)*math.pi*r*r*h
print("%.2f"%a)


