# Name: Justin Morrow
# Date: 03/08/2025
# Assignment: CSD325 Module 12.2 Redo Assignment (Module 2.2 "Documented Debugging + Flowchart(s)"
# Tasks: Use a program with at least one function, create a flowchart, capture debugging activity

# Function to greet the user
def hello_user(name):
# Inserting Pycharm debugger red dot on the below print statement line
    print(f"Hello {name},\n\nHave a nice day!")

# Input to collect the users name
name = input("Please enter your first name: ")

# Error checking for the user if an empty input or numeric value is entered.
while not name.isalpha() or not name.strip():
    if not name.strip():
        print("You didn't enter anything. Please enter a valid name.")
    elif not name.isalpha():
        print("Name should only contain letters. Please enter a valid name.")
    name = input("Please enter your first name: ")

# Capitalize the input for the users first name
cap_name = name.capitalize()

# Calling the hello_user function and passing the input entered by the user as the variable cap_name
hello_user(cap_name)

