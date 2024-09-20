"""Extend the given code (in the exercise area) so the code capitalizes all the names and surnames of the list and then prints the new list. The output of your code should be as below:

['John Smith', 'Jay Santi', 'Eva Kuki'] """

#Given code
names = ["john smith", "jay santi", "eva kuki"]

#My code
name2 = []

for name in names:
    name2.append(name.title())
    
print(name2)