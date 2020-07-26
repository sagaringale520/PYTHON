#FUnction Call Other function

def m1():
    print("This is First Function");
def m2():
    print("This is Second Function");
    m1()

m2()