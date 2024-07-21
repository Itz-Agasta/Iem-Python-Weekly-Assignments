# q1: Write a Python program to delete the last digit and print this. If input is
# 13613 then output is 3.

num = input("Enter a number: ")
len_num = len(num)
num_list = []
for _ in num:
    num_list.append(_)

print(num_list[len_num - 1])

# q2: Write a Python program to print the second last digit. If input is 427 then
# output is 2.
num = input("Enter a number: ")
len_num = len(num)
num_list = []
for _ in num:
    num_list.append(_)

print(num_list[len_num - 2])

# q3:  Write a Python program to exchange the last two digits. If input is 23617
# then output is 23671.
import re

num = input("Enter a number: ")
ans = re.sub(r'(\d)(\d)$', r'\2\1', num)

print(ans)

# q4: Write a Python program to read a number and find their product after
# exchanging last digits. If inputs are 348 and 31 then output is 12958
# (341*38).
# import re

num_1 = input("Enter a number: ")
num_2 = input("Enter another number: ")
new_num_1 = int(re.sub(r'(\d)(\d)$', r'\2\1', num_1))
new_num_2 = int(re.sub(r'(\d)(\d)$', r'\2\1', num_2))
ans = new_num_1 * new_num_2

print(ans)


# q5: Write a Python program to print the sum of last two digits. If input is 13613
# then output is 1+3=4
num = input("Enter a number: ")
ans = int(num[-1]) + int(num[-2])

print(ans)

