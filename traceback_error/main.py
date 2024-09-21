'''Simple program with errors that need to be handled'''

def function_a(x, y):
    print("Start a()")
    #Call b()
    function_b(x, y)

def function_b(x, y):
    print("Start b()")
    #Call c()
    function_c(x, y)

def function_c(x, y):
    print("Start c()")
    #Code with error: 42/0
    try:
        x / y
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        print(f"{x} divided by {y} equals {x/y}")

    print("Program has successfully completed.")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
             
function_a(num1, num2)
