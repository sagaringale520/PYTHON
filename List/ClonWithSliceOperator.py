#clone with slice operator

x=[10,20,30]
y=x[:]
print(x)
print(y)
print(id(x))
print(id(y))
x[1]=99
print(x)
print(y)
print(id(x))
print(id(y))
print(id(y))