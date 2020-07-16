#byte 0 -255

l2=[10,20,30,40,50,255]

b2=bytearray(l2)

print(b2)

print(type(b2))

#Reassign possible in byteArray beacause its mutable

b2[2]=60

print(b2)
#Its mutable we can reassign

#fetch data by index

print(b2[0])
print(b2[2])

#Iterate the Values
for i in b2 :
    print(i)

#value more that 255 is not support