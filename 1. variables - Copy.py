# Python Basics: Variables and Data Types

"""
Author: Kalim Amzad Chy
Email: kalim.amzad.chy@gmail.com

This Python script is designed to teach you the basics of variables and data types in Python.
We will cover:
1. What variables are and how to use them.
2. The basic data types in Python.
3. Variable naming conventions and industry standards.
4. Python's dynamic typing feature.

Each section includes explanations, examples, and assignments to reinforce your learning.
"""

# Section 1: Variables
# ---------------------
# Variables are containers for storing data values. In Python, a variable is created the moment you first assign a value to it.

# Example 1: Creating Variables
x = 5
y = "Hello, Python learners!"

# You can print the variables to see their values.
# print(x)
# print(y)

# Assignment 1: Create two variables, one holding a number and the other holding your name. Then print both.
# Write your code below:

age = 24
name = "Fariha"

# print("Age: ", age, end="; ")
# print("Name: ", name)

# Section 2: Data Types
# ---------------------
# Python has various data types including integers, float (decimal numbers), strings, booleans, and more.

# Example 2: Data Types
a = 5               # int
b = 3.14            # float
c = "Python"        # str
d = True            # bool

# You can check the type of any variable by using the type() function.
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

# Assignment 2: Create variables of different types and use the type() function to check their types.
# Write your code below:
integer_var = 10
float_var = 3.14
string_var = "Hello, world!"

print("Type of integer_var:", type(integer_var))
print("Type of float_var:", type(float_var))
print("Type of string_var:", type(string_var))


# Section 3: Variable Naming Conventions and Industry Standards
# -------------------------------------------------------------
"""
Variable names should be:
- Clear and descriptive.
- Start with a letter or an underscore.
- Only contain alpha-numeric characters and underscores (A-z, 0-9, and _).
- Case-sensitive (age, Age, and AGE are different variables).

Industry standards often follow the 'snake_case' naming style for variables in Python.
"""

# Example 3: Good and Bad Variable Names
good_name = "John"
_bad_name = 23
# 2bad = 42  # This will raise a SyntaxError because variable names cannot begin with a number.

good_name = "John"
_bad_name

# Assignment 3: Fix the bad variable name above and create three more variables with good naming practices.
# Write your code below:
age_years = 24
average_grade = 87.5
student_name = "Fariha Ahsan"

print("Type of age_ years:", type(age_years))
print("Type of average_grade:", type(average_grade))
print("Type of student_name:", type(student_name))



# Section 4: Python's Dynamic Typing
# ----------------------------------
# Python is dynamically typed, which means you don’t have to declare the type of variable while declaring it.

# Example 4: Dynamic Typing
var = "I am a string"
print(var)

var = 42
print(var)

# The variable 'var' changes type from str to int, demonstrating Python's dynamic typing.

# Assignment 4: Create a variable, assign it a value of one type, then reassign it to a different type and print both.
# Write your code below:


# Congratulations on completing this part of the Python workshop!
# Review the assignments, try to solve them, and check your understanding of variables and data types.
