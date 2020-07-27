#Global Keyword
a=5
def m1():
   global a
   a=3;
   print(a)

def m2():
    print(a)

m1()
m2()
