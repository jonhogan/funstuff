"""Extend the given code so the code prints out a list containing the number of characters for each username.

The output of your code should be as below:

    [9, 11, 11]"""

#Given code
usernames = ["john 1990", "alberta1970", "magnola2000"]

#My code
userNameLength= []

for name in usernames:
    userNameLength.append(len(name))
    
print(userNameLength)