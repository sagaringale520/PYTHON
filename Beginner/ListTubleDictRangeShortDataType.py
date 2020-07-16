l1=[10,20,100,200,3000]

print(l1)
print(type(l1))

for i in l1:
    print(i)

l1[2]=2000

print(l1)
#################
t1=(10,20,100,200,3000)

print(t1)
print(type(t1))

for i in t1:
    print(i)

#Reassignment not possible in tuple because of its immutable

#Range

r1=range(5)
r2=range(5,10)
r3=range(1,10,2)
print(r1)
for r in r1:
    print(r)
for r in r2:
    print(r)
for r in r3:
    print(r)

#Dict {}

d1={10,20,33,40}
print(d1)
for d in d1:
    print(d)

#it reads in random ways
