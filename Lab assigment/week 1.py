# 1. Write a Python program that asks the user for his name and then welcomes him.
name = input("Enter your name: ")
print("Welcome", name)


# 2. Write a Python program that accepts principle, rate, and time from the user and
# prints the simple interest
principle = float(input("Enter principle amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time: "))

simple_interest = (principle * rate * time) / 100

print("Simple interest is: ", simple_interest)


# 3. Write a Python program that prompts the user to input principle, rate, and time
# and calculate compound interest.
principle = float(input("Enter principle amount: "))
rate = float(input("Enter rate of interest: "))
n = int(input("Enter Compound interest rate.(daily, monthly, quarterly, half-year, yearly) "))
time = float(input("Enter time: "))

compound_interest = principle * (pow((1 + (rate / 100)/n), n * time))
print(f"Compound interest is: {compound_interest} rs") # (https://byjus.com/maths/compound-interest/)


# 4. Write a program in Python to calculate the area and perimeter of various
# polygons such as triangles, rectangles, and circles.
import math

def triangle_area(base, height):
    return 0.5 * base * height

def triangle_perimeter(a, b, c):
    return a + b + c

def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)

def circle_area(radius):
    return math.pi * radius * radius

def circle_perimeter(radius):
    return 2 * math.pi * radius

# Example usage:
print("Triangle area:", triangle_area(5, 10))
print("Triangle perimeter:", triangle_perimeter(3, 4, 5))

print("Rectangle area:", rectangle_area(4, 6))
print("Rectangle perimeter:", rectangle_perimeter(4, 6))

print("Circle area:", circle_area(7))
print("Circle perimeter:", circle_perimeter(7))


# 5. Write a program in Python to input 3 numbers separated by comma, and find the
# largest and smallest among them.
numbers = list(map(int, input("Enter 3 numbers separated by comma: ").split(",")))
large_num = max(numbers)
small_num = min(numbers)
print(f"Largest number is: {large_num} \nSmallest number is: {small_num}")


# 6. Write a program in Python to find the roots of a quadratic equation using Python.
import math


def find_roots(a, b, c): # Ref: https://www.programiz.com/cpp-programming/examples/quadratic-roots
    """
    Calculate the roots of a quadratic equation ax^2 + bx + c = 0.

    Parameters:
    a (float): Coefficient of x^2
    b (float): Coefficient of x
    c (float): Constant term

    Returns:
    tuple: A tuple containing the roots. If the roots are real, it returns two real numbers.
           If the roots are complex, it returns two tuples, each containing the real and imaginary parts.
    """
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root, root
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        return (real_part, imaginary_part), (real_part, -imaginary_part)

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

roots = find_roots(a, b, c)
print("The roots of the quadratic equation are:", roots)


# 7. Write a program in Python to print all prime numbers inside a range of numbers
# provided by the user.
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1): # Iterate from 2 to the square root of num (inclusive).
            # This is an optimization to reduce the number of checks needed to determine if num is prime
            if num % i == 0:
                break
        else:
            print(num)


# 8. Write a program in Python to print the mean and standard deviation of 5 scores
# input by the user.
import math

scores = list(map(float, input("Enter 5 scores separated by spaces: ").split()))

mean = sum(scores) / len(scores) # Calculate the mean
variance = sum((x - mean) ** 2 for x in scores) / len(scores) # Calculate the standard deviation
# For Example: For the scores [85.0, 90.0, 78.0, 92.0, 88.0] and mean 86.6, the variance is ((85.0 - 86.6) ** 2
# + (90.0 - 86.6) ** 2 + (78.0 - 86.6) ** 2 + (92.0 - 86.6) ** 2 + (88.0 - 86.6) ** 2) / 5 = 28.24.
std_deviation = math.sqrt(variance)

print(f"Mean: {mean} \n Standard Deviation: {std_deviation}")


# 9. Write a program in Python to create a calculator that can perform basic arithmetic operations.
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def calculator():
    """
    Perform basic arithmetic operations based on user input.

    Prompts the user to select an operation and input two numbers,
    then performs the selected operation and prints the result.
    """
    print("Select operation: \n 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"The result is: {add(num1, num2)}")
    elif choice == '2':
        print(f"The result is: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"The result is: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"The result is: {divide(num1, num2)}")
    else:
        print("Invalid input")

calculator()


# 10. Write a program in Python to convert temperatures between Celsius and Fahrenheit.
print("Select conversion type: \n 1. Celsius to Fahrenheit \n 2. Fahrenheit to Celsius")
choice = input("Enter choice (1/2): ")

if choice == '1':
    # Convert Celsius to Fahrenheit
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F")
elif choice == '2':
    # Convert Fahrenheit to Celsius
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is equal to {celsius}°C")
else:
    print("Invalid input")


# 11. Write a program in Python to check whether an input is even or odd.
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")


# 12. Write a program in Python to check whether an input is leap year or not.
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


# 13.  Write a python program that prompts the user to enter a number and determines
# whether it is positive, negative, or zero.
number = float(input("Enter a number: "))

if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is zero")


# 14. Write a program that prompts the user to enter their age and prints the
# corresponding age group. The program should use the following age groups:
# 0-12: Child
# 13-19: Teenager
# 20-59: Adult
# 60 and above: Senior Citizen
age = int(input("Enter your age: "))

if 0 <= age <= 12:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
elif 20 <= age <= 59:
    print("Adult")
elif age >= 60:
    print("Senior Citizen")
else:
    print("Invalid age")

# 15. Write a program that prompts the user to enter their weight (in kilograms) and
# height (in meters). The program should calculate the Body Mass Index (BMI)
# using the formula: BMI = weight / (height * height). The program should then
# classify the BMI into one of the following categories:
# less than 18.5 - Underweight
# BMI between 18.5 and 24.9 - Normal weight
# BMI between 25 and 29.9 - Overweight
# BMI 30 or greater - Obesity
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height * height)

if bmi < 18.5:
    classification = "Underweight"
elif 18.5 <= bmi <= 24.9:
    classification = "Normal weight"
elif 25 <= bmi <= 29.9:
    classification = "Overweight"
else:
    classification = "Obesity"

print(f"Your BMI is {bmi:.2f}, which is classified as {classification}.")
