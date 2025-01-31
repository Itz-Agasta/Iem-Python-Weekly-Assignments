# Write a program to create a text file as per the path and filename provided by the user and add
# text as input by the user.
import os
def create_and_write_file():
    file_path = input("Enter the path where you want to create the file: ")
    text_to_write = input("Enter the text you want to write into the file: ")
    file_name = input("what will be your file name: ")
    file = os.path.join(file_path, file_name)

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    with open(file, 'w') as file:
        file.write(text_to_write)
    print(f"File created and text written to {file_path}")


create_and_write_file()

# Write a program to copy the content of a text file to another file but while copying convert all
# capital letters to small letters.
def copy_and_convert_file():
    # Get the source file path from the user
    source_file_path = input("Enter the path of the source file: ")
    
    # Get the destination file path from the user
    destination_file_path = input("Enter the path of the destination file: ")
    
    try:
        # Open the source file in read mode
        with open(source_file_path, 'r') as source_file:
            # Read the content of the source file
            content = source_file.read()
        
        # Convert the content to lowercase
        converted_content = content.lower()
        
        # Open the destination file in write mode
        with open(destination_file_path, 'w') as destination_file:
            # Write the converted content to the destination file
            destination_file.write(converted_content)
        
        print(f"Content copied and converted to lowercase in {destination_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
copy_and_convert_file()

# Create a text file to append N lines such that each line displays the Fibonacci sequence upto
# the term corresponding to specific line number separated by ‘-’. For N = 5 the text file should
#read.
#1
#1-1
#1-1-2
#1-1-2-3
# 1-1-2-3-5

def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(b)
        a, b = b, a + b
    return sequence

def append_fibonacci_to_file():
    # Get the file path and name from the user
    file_path = input("Enter the path and filename where you want to create the file: ")
    
    # Get the number of lines (N) from the user
    N = int(input("Enter the number of lines (N): "))
    
    try:
        # Open the file in append mode
        with open(file_path, 'a') as file:
            for i in range(1, N + 1):
                # Generate the Fibonacci sequence up to the i-th term
                sequence = fibonacci_sequence(i)
                # Convert the sequence to a string with '-' separator
                line = '-'.join(map(str, sequence))
                # Write the line to the file
                file.write(line + '\n')
        print(f"Fibonacci sequence up to {N} lines appended to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
append_fibonacci_to_file()

""" 
Take input four values from user with respect to number of books, pens, bags and total price
as follows. 36, 116, 23, 4649 and save it as a text file
Books: 36
Pens: 116
Bags : 23
Price : Rs. 4649
"""
def save_items_to_file():
    # Get the file path and name from the user
    file_path = input("Enter the path and filename where you want to save the details: ")
    
    # Get the number of books, pens, bags, and total price from the user
    books = input("Enter the number of books: ")
    pens = input("Enter the number of pens: ")
    bags = input("Enter the number of bags: ")
    price = input("Enter the total price: ")
    
    try:
        # Open the file in write mode
        with open(file_path, 'w') as file:
            # Write the details to the file
            file.write(f"Books: {books}\n")
            file.write(f"Pens: {pens}\n")
            file.write(f"Bags: {bags}\n")
            file.write(f"Price: Rs. {price}\n")
        print(f"Details saved to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
save_items_to_file()

"""
Write a program to create a dictionary by reading records from the text file output in program
4th
Dictionary : {“Books”:36, “Pens”: 116, “Bags”:23, “Price”: “4649”}
"""
def create_dictionary_from_file():
    # Get the file path from the user
    file_path = input("Enter the path and filename of the text file: ")
    
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read the lines from the file
            lines = file.readlines()
        
        # Create a dictionary from the lines
        records = {}
        for line in lines:
            key, value = line.strip().split(': ')
            records[key] = value
        
        print(f"Dictionary: {records}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
create_dictionary_from_file()


# Write a program to take inputs from user to create a dictionary for storing and displaying
# student data
def create_student_dictionary():
    # Create an empty dictionary to store student data
    student_data = {}
    
    # Get student details from the user
    student_data['Name'] = input("Enter the student's name: ")
    student_data['Age'] = input("Enter the student's age: ")
    student_data['Grade'] = input("Enter the student's grade: ")
    student_data['School'] = input("Enter the student's school: ")
    
    # Display the student data
    print("Student Data:")
    for key, value in student_data.items():
        print(f"{key}: {value}")

# Call the function
create_student_dictionary()

# Store the dictionary data as a CSV file and write a function to display the data from the CSV
# file.
import csv

def create_student_dictionary():
    # Create an empty dictionary to store student data
    student_data = {}
    
    # Get student details from the user
    student_data['Name'] = input("Enter the student's name: ")
    student_data['Age'] = input("Enter the student's age: ")
    student_data['Grade'] = input("Enter the student's grade: ")
    student_data['School'] = input("Enter the student's school: ")
    
    # Store the dictionary data as a CSV file
    file_path = input("Enter the path and filename to save the CSV file: ")
    try:
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for key, value in student_data.items():
                writer.writerow([key, value])
        print(f"Student data saved to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def display_csv_data():
    # Get the file path from the user
    file_path = input("Enter the path and filename of the CSV file: ")
    
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            print("Student Data from CSV:")
            for row in reader:
                print(f"{row[0]}: {row[1]}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the functions
create_student_dictionary()
display_csv_data()

"""Write a function to update or delete a specific record in student database csv file.
"""
import csv

def create_student_dictionary():
    # Create an empty dictionary to store student data
    student_data = {}
    
    # Get student details from the user
    student_data['Name'] = input("Enter the student's name: ")
    student_data['Age'] = input("Enter the student's age: ")
    student_data['Grade'] = input("Enter the student's grade: ")
    student_data['School'] = input("Enter the student's school: ")
    
    # Store the dictionary data as a CSV file
    file_path = input("Enter the path and filename to save the CSV file: ")
    try:
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for key, value in student_data.items():
                writer.writerow([key, value])
        print(f"Student data saved to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def display_csv_data():
    # Get the file path from the user
    file_path = input("Enter the path and filename of the CSV file: ")
    
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            print("Student Data from CSV:")
            for row in reader:
                print(f"{row[0]}: {row[1]}")
    except Exception as e:
        print(f"An error occurred: {e}")

def update_or_delete_record():
    # Get the file path from the user
    file_path = input("Enter the path and filename of the CSV file: ")
    
    # Read the existing data
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            records = list(reader)
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    
    # Get the record to update or delete
    key_to_modify = input("Enter the key of the record to update or delete: ")
    
    # Find the record
    record_found = False
    for record in records:
        if record[0] == key_to_modify:
            record_found = True
            action = input("Enter 'update' to update the record or 'delete' to delete the record: ").strip().lower()
            if action == 'update':
                new_value = input(f"Enter the new value for {key_to_modify}: ")
                record[1] = new_value
            elif action == 'delete':
                records.remove(record)
            else:
                print("Invalid action.")
            break
    
    if not record_found:
        print(f"No record found with key: {key_to_modify}")
        return
    
    # Write the updated data back to the file
    try:
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(records)
        print(f"Record {action}d successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the functions
create_student_dictionary()
display_csv_data()
update_or_delete_record()

# Write a program to print all elements in a list those have only single occurrence.
def print_single_occurrence_elements():
    # Get the list of elements from the user
    elements = input("Enter the elements of the list separated by spaces: ").split()
    
    # Create a dictionary to count occurrences of each element
    occurrence_count = {}
    for element in elements:
        if element in occurrence_count:
            occurrence_count[element] += 1
        else:
            occurrence_count[element] = 1
    
    # Print elements that have only a single occurrence
    print("Elements with a single occurrence:")
    for element, count in occurrence_count.items():
        if count == 1:
            print(element)

# Call the function
print_single_occurrence_elements()

"""
Write a program to read 6 numbers and create a dictionary having keys EVEN and ODD.
Dictionary's value should be stored in list. Your dictionary should be like: {'EVEN':[8,10,64],
'ODD':[1,5,9]}.
"""
def create_even_odd_dictionary():
    # Get 6 numbers from the user
    numbers = []
    for i in range(6):
        number = int(input(f"Enter number {i+1}: "))
        numbers.append(number)
    
    # Create a dictionary to store even and odd numbers
    even_odd_dict = {'EVEN': [], 'ODD': []}
    
    # Separate the numbers into even and odd lists
    for number in numbers:
        if number % 2 == 0:
            even_odd_dict['EVEN'].append(number)
        else:
            even_odd_dict['ODD'].append(number)
    
    # Print the dictionary
    print(f"Dictionary: {even_odd_dict}")

# Call the function
create_even_odd_dictionary()