#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    """ function that removes all characters c and C from a string."""
    new_string = ''.join(
            char for char in my_string if char != 'c' and char != 'C'
            )
    return (new_string)
