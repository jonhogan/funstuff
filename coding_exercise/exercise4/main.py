"""Extend the given code so it prints out the sum of the numbers.

The output of your code should be as below:

    49.1"""

#Given code
user_entries = ['10', '19.1', '20']

#My code

sum = 0.0

for entry in user_entries:
    sum = sum + float(entry)

print(sum)