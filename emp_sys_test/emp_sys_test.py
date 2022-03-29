# Title: Employee Management System Program
# Program created by William Schaeffer
# CPS 313
# P. 581, Exercise 7, emp_sys_test.py
# 03.15.22

# This program will store Employee objects in a dictionary with employee ID number as the key
    # The program should present a menu that lets the user look up, add new, change, delete, or quit

# imports for functions, classes

import emp, sys_func, pickle, os.path

# Global Constants 
    # for menu choices
ADD = 1
CHANGE = 2
DELETE = 3
LOOKUP = 4
QUIT = 5

# Main Function

def main():
   
    choice = 0                                              # initialize user choice
    eof = False                                             # to indicate end of file

    if os.path.exists('employee_list.pickle'):              # check to see if file exists, if it does, open as read and 
        employee_file = open('employee_list.pickle', 'rb')
        while not eof:
            try:
                employees = pickle.load(employee_file)

            except EOFError:                                # Set the flag to indicate the end of the file has been reached
                eof = True

    else:
        employee_file = open('employee_list.pickle', 'wb')  # create the .pickle if it doesn't exist
        employees = {}                                      # initialize empty dictionary for email addresses. key:value, name:email


    employee_file.close()                                   # close the file

    while choice != QUIT:
        choice = sys_func.get_menu_choice()                 # display choices and get choice from user
                                                          
        if choice == ADD:
            employees = sys_func.add(employees)
        elif choice == CHANGE:
            employees = sys_func.change(employees)
        elif choice == DELETE:
            employees = sys_func.delete(employees)
        elif choice == LOOKUP:
            sys_func.lookup(employees)

    print('Pickling the employee dictionary, saving the file, and closing the file and program.')

    employee_file = open('employee_list.pickle', 'wb')      # reopen address_file

    pickle.dump(employees, employee_file)                   # put pickled dictionary into address_file
    
    employee_file.close()

if __name__ == '__main__':
    main()                                                  # call main function
