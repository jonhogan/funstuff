"""Extend the given code so the code prints out a list containing the same items as floats.

The output of your code should be as below:

    [10.0, 19.1, 20.0]"""

#Given Code

user_entries = ['10', '19.1', '20']

#My Code
float_entries = [float(entry) for entry in user_entries]

print(float_entries)