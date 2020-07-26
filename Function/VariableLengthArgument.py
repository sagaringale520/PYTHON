#vAriable lenght argument

def sum(x,*y):
    print(type(x))
    print(type(y))
    for i in y:
        print(i)

sum(1,2,3,4,5)
sum(10,20,30,40)