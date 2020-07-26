# Pass function as a parameter to another function.

def m1(a):
    print("This  is firt message")

def m2():
    print("This is second Function")

m1(m2())

