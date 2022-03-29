# Title: Employee Class
# Program created by William Schaeffer
# CPS 313
# P. 581, Exercise 7, emp_sys_test.py
# 03.15.22

# This Class will hold data attributes for an employee

# imports for functions, classes

# Employee Class

class Employee:

# method for initializing data attributes
    # This initializing function accepts the employee's 
    # name, ID, department, and job title as arguments. 

    def __init__(self, name, id, dept, title):
        self.__name = name
        self.__identification = id
        self.__department = dept
        self.__job_title = title

# mutator methods

    def set_name(self, name):
        self.__name = name

    def set_identification(self, id):
        self.__identification = id

    def set_department(self, dept):
        self.__department = dept

    def set_title(self, title):
        self.__job_title = title

# accessor methods
    
    def get_name(self):
        return self.__name

    def get_identification(self):
        return self.__identification

    def get_department(self):
        return self.__department
    def get_title(self):
        return self.__job_title

# additional methods

    # display object state
    
    def __str__(self):
        return f'Name: {self.__name}\nID number: {self.__identification}\nDepartment: {self.__department}\nTitle: {self.__job_title}'