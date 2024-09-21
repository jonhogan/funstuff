'''Simple program with errors that need to be handled'''

def function_a():
    print("Start a()")
    #Call b()
    function_b()

def function_b():
    print("Start b()")
    #Call c()
    function_c()

def function_c():
    print("Start c()")
    #Code with error: 42/0
    try:
        42 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero!")

    print("Program has successfully completed.")

function_a()
