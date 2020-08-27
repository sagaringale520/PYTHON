#list comparison > < >= <=

print([1,2,3]==[1,2,3])
print([1,2,3]<[1,2,3])
print([1,2,3]<=[1,2,3])
print([1,2,1]<=[1,2,3])
print([1,2,1]>=[1,2,3])
print([1,2,1]>[1,2,3])
print([1,2,1]!=[1,2,3])

x =["abc", "def", "ghi"]
y =["abc", "def","ghi"]
z =["ABC", "DEF", "GHI"]
a =["abc", "def", "ghi", "jkl"]
print(x==y) # True
print(x==z) # False
print(x==a) # False