#Copy list with Copy method

x=[10,20,30]
y=x.copy()

print(id(x))
print(id(y))

print(x)
print(y)

x[1]=99
print(x)
print(y)
