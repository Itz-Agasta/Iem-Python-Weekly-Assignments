# 1: Write a Python program, which reads a, b and c as sides of a triangle and prints area.
from math import sqrt

a = int(input("what is the value of side a: "))
b = int(input("what is the value of side b: "))
c = int(input("what is the value of side c: "))


def area_cal(x, y, z):
    s = ((x + y + z) / 2)
    area = sqrt(s * (s - x) * (s - y) * (s - z))
    print(round(area, 2))


area_cal(a, b, c)

# 2: Write a Python program that accepts principle, rate and time from the user and print the simple interest.
p = int(input("what is the principle amount: "))
r = float(input("what is the rate: "))
t = int(input("For how much time: "))

interest = round((p * r * t), 2)

print(f"your interest is {interest} rs")

# 3:  Write a Python program that prompts the user to input principle, rate, and
# time and calculate compound interest.
p = int(input("what is the principle amount: "))
r = float(input("what is the rate: "))
n = int(input("you are compounding for: "))
t = int(input("For how much time: "))

amount = round(p * (pow((1 + r / n), n * t)), 2)
ci = (amount - p)

print(f"your compound interest after {t} years will be {ci}")

# 4: Write a Python program, which reads x1, y1, x2 and y2 and finds distance
# between points (x1, y1) and (x2, y2). If input 3(x1), 7(y1), 11(x2), 13(y2)
# then output 10.

# from math import sqrt
x1 = int(input("what is the x1: "))
y1 = int(input("what is the y1: "))
x2 = int(input("what is the x2: "))
y2 = int(input("what is the y2: "))

distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(distance)

# 5: Write a Python program, which reads a, b, and c. Let ax + by + c = 0 be
# equation of a line. Print the slope. If input 3, 5, 8 then output -0.6.
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))


def slop_cal(x, y):
    if y == 0:
        return "Undefined (vertical line)"
    return -x / y


slop = slop_cal(a, b)
print(f"The slope of the line is:{slop}")
