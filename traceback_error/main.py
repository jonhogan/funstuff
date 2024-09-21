'''Simple program with errors that need to be handled'''

def a():
    print("Start a()")
    #Call b()
    b()

def b():
    print("Start b()")
    #Call c()
    c()

def c():
    print("Start c()")
    #Code with error: 42/0
    42 / 0

a()