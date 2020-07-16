#byte 0 -255

l1=[10,20,30,40,50]

b1=bytes(l1)

print(b1)

print(type(b1))

#Its immutable we can not reassign

#fetch data by index

print(b1[0])
print(b1[2])

#Iterate the Values
for i in b1 :
    print(i)