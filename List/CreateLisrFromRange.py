#list compresiation

squares = [x**2 for x in range(1, 11)]
print(squares)

s=range(1, 20, 3)
for i in s:
    print(i)
m=[y for y in s if y%2==0]
print(m)