#FUnction generator

def msg1():
    yield "Sagar"
    yield "Ingale"

x=msg1()
print(type(x))
print(x)

for i in x:
    print(i)