#Decor Function

def m1(number):
    def m2():
        x = number()
        return x + 2
    return m2
def m3():
    return 10
result = m1(m3)
print(result())

