#Globals Method

a=20

def m1():
    a=2;
    print(a)
    print(globals()['a'])

def m2():
    print(a)

m1()
m2()