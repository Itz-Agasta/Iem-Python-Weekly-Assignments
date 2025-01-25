#1. Write a Python program that prompts the user to input a number from 1 to 7. The program
# should display the corresponding day for the given number. For example, if the user types 1
Days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
number = int(input("Enter a number from 1 to 7: "))

if number < 1 or number > 7:
    print("Invalid number")
else:
    print(Days[number - 1])

#2. Write a Python program that prompts the user to input the number of calls and calculate the
# monthly telephone bills as per the following rule:
# Minimum Rs. 200 for up to 100 calls.
# Plus Rs. 0.60 per call for the next 50 calls.
# Plus Rs. 0.50 per call for the next 50 calls.
# Plus Rs. 0.40 per call for any call beyond 200 calls.
# Get number of calls from user
calls = int(input("Enter number of calls: "))
bill = 200  # Base charge

if calls <= 100:
    pass  # Only base charge applies
elif calls <= 150:
    bill += (calls - 100) * 0.60  # Charge for calls from 101-150
elif calls <= 200:
    bill += 50 * 0.60  # First 50 calls after 100
    bill += (calls - 150) * 0.50  # Remaining calls up to 200
else:
    bill += 50 * 0.60  # First 50 calls after 100
    bill += 50 * 0.50  # Next 50 calls
    bill += (calls - 200) * 0.40  # Remaining calls beyond 200

print(f"Total bill: Rs. {bill:.2f}")


#3. Write a program in Python to calculate the factorial of a number.
number = int(input("Enter a number: "))
factorial = 1

if number < 0:
    print("Factorial does not exist for negative numbers")
elif number == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, number + 1):
        factorial *= i
    print(f"The factorial of {number} is {factorial}")

# 4. Write a program in Python to calculate the Fibonacci sequence till a specific no. of terms.
terms = int(input("Enter the number of terms: "))

n1, n2 = 0, 1
count = 0

if terms <= 0:
    print("Please enter a positive integer")
elif terms == 1:
    print("Fibonacci sequence up to", terms, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < terms:
        print(n1)
        nth = n1 + n2
        # Update values
        n1 = n2
        n2 = nth
        count += 1

#5. Write a program in Python to calculate the factors of numbers.
number = int(input("Enter a number: "))

print(f"The factors of {number} are:")
for i in range(1, number + 1):
    if number % i == 0:
        print(i)

#6. Write a program in Python to calculate the magic square based on a given number.
n = int(input("Enter an odd number: "))

if n % 2 == 0:
    print("Please enter an odd number")
else:
    magic_square = [[0] * n for _ in range(n)]

    num = 1
    i, j = 0, n // 2

    while num <= n * n:
        magic_square[i][j] = num
        num += 1
        newi, newj = (i - 1) % n, (j + 1) % n

        if magic_square[newi][newj]:
            i += 1
        else:
            i, j = newi, newj

    print("Magic Square:")
    for row in magic_square:
        print(row)

#7. Write a program in Python to check if a number is a palindrome.
number = input("Enter a number: ")
rev_number = number[::-1]

if number == rev_number:
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")

#8. Write a program in Python to check if a number is an Armstrong number.
number = int(input("Enter a number: "))
sum = 0
num_digits = len(str(number))

for digit in str(number):
    sum += int(digit) ** num_digits

if number == sum:
    print(f"{number} is an Armstrong number")    
else:
    print(f"{number} is not an Armstrong number")

#Note: https://www.outsystems.com/forums/discussion/87853/armstrong-numbers/#Post417562


#8. Write a program in Python to check if a number is Krishnamurthy number.
import math

number = int(input("Enter a number: "))
sum_of_factorials = 0

for digit in str(number):
    sum_of_factorials += math.factorial(int(digit))

if number == sum_of_factorials:
    print(f"{number} is a Krishnamurthy number")
else:
    print(f"{number} is not a Krishnamurthy number")


#9. Write a program in Python to find the sum of digits of a number.
number = int(input("Enter a number: "))
sum = 0

for digits in number:
    sum += int(digits)
print(f"The sum of digits of {number} is {sum}")

#10. Write a program in Python to reverse a given number.
number = int(input("Enter a number: "))
rev_number = str(number[::-1])
print(f"The reverse of {number} is {rev_number}")

#11. Write a program in Python to find the sum of squares of the first n natural numbers.
n = int(input("Enter a number: "))
sum_of_squares = 0

for i in range(1, n + 1):
    sum_of_squares += i ** 2

print(f"The sum of squares of the first {n} natural numbers is {sum_of_squares}")


#11. Write a program in Python to convert a decimal number to a binary number.
decimal_number = int(input("Enter a decimal number: "))
binary_number = ""

if decimal_number == 0:
    binary_number = "0"
else:
    while decimal_number > 0:
        binary_number = str(decimal_number % 2) + binary_number
        decimal_number //= 2

print(f"The binary representation is {binary_number}")

#12. Write a program in Python that prompts the user to input a number and prints its
# multiplication table.
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

#13. Write a Python program to print the first 6 terms of a geometric sequence starting with 2 and
# having a common ratio of 3.
start = 2
ratio = 3
terms = 6

current_term = start
for _ in range(terms):
    print(current_term)
    current_term *= ratio
