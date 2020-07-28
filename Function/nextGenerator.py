#NextGenerator

def msg():
    yield "Sagar"
    yield "Rajendra"
    yield "Ingale"

x=msg()
print(type(msg()))

print(type(x))

print(next(x))
print(next(x))
print(next(x))

print(id(x))

