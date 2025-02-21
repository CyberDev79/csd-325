# Name: Justin Morrow
# Date: 02/20/2025
# Assignment: CSD325 Module 8.2 "JSON Practice"
# Purpose: Create flowchart based on requirements, then write a Python program that produces the required results
# Reference: Stack Overflow. (2013, November 18). Python read JSON file and modify. Stack Overflow.
#   https://stackoverflow.com/questions/21035762/python-read-json-file-and-modify
# Reference: GeeksforGeeks. (2021, December 10). Modify JSON fields using Python. GeeksforGeeks.
#    https://www.geeksforgeeks.org/modify-json-fields-using-python/
# Reference: W3Schools. (n.d.). Python string isalpha() method. W3Schools.
#    https://www.w3schools.com/python/ref_string_isalpha.asp


# Import JSON module for interacting with the student.json file
import json


# This function will read the data in the JSON student file and save it to a list
def load_students(json_student_file):
    with open(json_student_file, 'r') as js_file:
        return json.load(js_file)

# This function will be used for calling a print out of the student list concatenated on a single line
def print_students(students):
    for student in students:
        print(f"{student['F_Name']} {student['L_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")


# This function is used for both the first and last name prompts. It validates against blank and accepts alphabetic only
def get_name(prompt):
    while True:
        name = input(prompt).strip().capitalize()
        if name == "":
            print("The name can't be blank. Please enter a name.")
        elif not name.isalpha():
            print("Names can be entered as text only. Please enter text only A-Z.")
        else:
            return name


# This function is used to get a valid Student ID as a numeric/integer value and not blank
def get_student_id():
    while True:
        try:
            student_id = int(input("Enter Student ID: ").strip())
            return student_id
        except ValueError:
            print("You entered an incorrect Student ID. Please enter using numbers only for the Student ID")


# This function is used to get valid Email Address by validating it's not blank and contains both "@" and "."
def get_email():
    while True:
        email = input("Enter the Students Email Address: ").strip()
        if "@" not in email or "." not in email:
            print("You entered an incorrect email address. Please Re-enter a valid email (Ex: text@test.com)")
        else:
            return email


# This is the main function
def main():
    json_student_file = 'student.json' # Defines the JSON file as student.json and must be in same directory as .py file
    students = load_students(json_student_file) # Calls the load_students function and stores it as students

    # Print out the current Student list before making any changes
    print("\nHere is the current Student list\n")
    print_students(students)

    # Interactive Prompt for the user to enter the new student information
    print("\nEnter the details for the new student below.\n")
    first_name = get_name("Enter First Name: ") # Text prompt here to reuse get_name function for both first/last name
    last_name = get_name("Enter Last Name: ") # Text prompt here to reuse get_name function for both first/last name
    student_id = get_student_id() # calls the get_student_id function which has the prompt and returned as student_id
    email = get_email() # calls the get_email function which has the prompt and returned as email

    # Create new_student dictionary with new student details from the user input, then append/add to the students list
    new_student = {"F_Name": first_name, "L_Name": last_name, "Student_ID": student_id, "Email": email}
    students.append(new_student)

    # Print the updated student list using the dictionary keys for each student and calling the print_students function
    print(f"\nHere is the updated Student list after adding the new student: {first_name} {last_name}\n")
    print_students(students)

    # Overwrite 'w' the student.json file with all the contents of the Python student list using json.dump
    with open(json_student_file, 'w') as js_file:
        json.dump(students, js_file, indent=4) # indent=4 (pretty-printed format)

    # Closing print statement
    print("\nThe student.json file has been successfully updated with the new student record. Thank you!")

if __name__ == '__main__':
    main()
