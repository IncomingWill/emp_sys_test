# Title: Employee Management System Program Functions
# Program created by William Schaeffer
# CPS 313
# P. 581, Exercise 7, emp_sys_test.py
# 03.15.22

# This file will hold functions for emp_sys_test.py

# imports for functions, classes

import emp

# Functions

# Global Constants 
    # for menu choices
ADD = 1
CHANGE = 2
DELETE = 3
LOOKUP = 4
QUIT = 5

# Function to display and return menu choice

def get_menu_choice():
    print()
    print('Employee Management System')
    print('#========================#')
    print('1. Add Employee')
    print('2. Change Employee')
    print('3. Delete Employee')
    print('4. Look Up Employee')
    print('5. Quit Program')
    print()

    choice = int(input('Enter your choice: '))

    while choice < ADD or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    return choice

# Function to add employee to dictionary
    # if ID not in dictionary, add employee to dictionary
    # if ID is in dictionary, display warning

def add(emp_dict):
    
    print()
    name = input('Enter a name: ')
    id = input('Enter an employee ID: ')
    dept = input('Enter an employee department: ')
    title = input('Enter an employee job title: ')

    new_employee = emp.Employee(name, id, dept, title)

    if id not in emp_dict:
        emp_dict[id] = new_employee
        print()
        print('Added new employee:')
        print(new_employee)
   
    if id in empt_dict:

        print('That Employee ID already exists, cannot have duplicates.')

    return emp_dict

# Function to pull the employee to be changed out of dictionary
    # Pulled employee and dictionary are passed to change_details function
    # Displays changed details and returns the dictionary

def change(emp_dict):
    
    id = input('Enter an Employee ID: ')

    if id in emp_dict:
       
        employee = emp_dict[id]                                             #pull employee to change from dictionary
        employee, emp_dict = change_details(employee, emp_dict)             #emp_dict only passed for changing id
        print()
        print('Changed employee details:')                                  #display changed details
        print(employee)

    if id not in emp_dict:

        print('That Employee ID is not found.')

    return emp_dict

# Function to make the changes to employee
    # Each choices only changes the employee details
    # Exception is changing the ID, which then also pops the old entry and replaces it with new entry
    # returns employee and dictionary

def change_details(emp, emp_dict):

    print('Which of the following Employee Details would you like to change?')
    print('Please type in one of the following options: ')
    choice = input('Name, ID, Department, or Title: ').upper()              #choice to upper for selection

    if choice == 'NAME':
        print()
        new_name = input('Please enter new name: ')
        emp.set_name(new_name)                                              #set a new name for employee

    elif choice == 'ID':
        print()
        new_id = input('Please enter new ID: ')

        if new_id in emp_dict:                                              #if id in dictionary, exit function
            print('That Employee ID already exists, cannot have duplicates.')
            print('Please Try again.')
            return emp, emp_dict

        old_id = emp.get_identification()                                   #grab old id before deletion
        emp_dict.pop(old_id)                                                #delete old entry via pop()
        emp.set_identification(new_id)                                      #set new id to employee
        emp_dict[new_id] = emp                                              #add changed id and employee to dictionary

    elif choice == 'DEPARTMENT':
        print()
        new_dept = input('Please enter new department: ')
        emp.set_department(new_dept)                                        #set a new department for employee

    elif choice == 'TITLE':
        print()
        new_title = input('Please enter new title: ')
        emp.set_title(new_title)                                            #set a new title for employee

    else:
        print()
        print('Improper input. Please try again')

    return emp, emp_dict

# Function to delete an employee entry in the dictionary
    # Returns the dictionary

def delete(emp_dict):

    id = input('Enter an Employee ID: ')
    print()

    if id in emp_dict:
        print('Deleting the following employee:')
        print()
        print(emp_dict[id])
        del emp_dict[id]                                                    #delete employee in dictionary
        print()
        print('Employee Deleted.')
    
    if id not in emp_dict:

        print('That Employee ID is not found.')

    return emp_dict

# Function to look up and display employee entry in dictionary

def lookup(emp_dict):

    id = input('Enter an Employee ID: ')
    print()

    if id in emp_dict:
       
        print('Employee Lookup retrieved: ')
        print()
        print(emp_dict[id])                                                 #display employee object state
    
    if id not in emp_dict:

        print('That Employee ID is not found.')