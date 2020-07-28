def m1(n):
    def m2():
        value = n()
        return value + 2
    return m2
@m1
def m3():
    return 10
print(m3())