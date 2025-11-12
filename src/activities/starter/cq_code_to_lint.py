"""Poorly formatted code.
This module contains a function that will be linted in activity 3.6
"""

globalTEST = 'This is a global variable'


def in_correct_function_name():
    print('This is a function with a poorly formatted name')


def missing_docstring(message):
    print(message)
    print("This is a function that is missing it's docstring")
    result = "message printed"
    return result


def incorrect_spacing_between_functions():
    print('This function has incorrect spacing from the function above')


def incorrect_spacing_duplicate():
    print("This is a duplicated function name")


def incorrect_whitespace(x, y):
    result = x + y
    print(result)
    return result
