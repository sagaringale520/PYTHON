#Function Inside Function

def m1():
    print("This is the Outer Function")
    def m2():
        print("This is Inner Function")
    m2()

m1()