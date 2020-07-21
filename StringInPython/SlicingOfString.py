#Slicing Cases of string

Str1="Hello World"

print(len(Str1))

print(Str1[:])      #Start from 0 to n-1
print(Str1[::])      #Start from 0 to n-1 and step is 1
print(Str1[:10:1])      #Start from 0 to 9 and step is 1
print(Str1[2::1])      #Start from 2 to 10 and step 1
print(Str1[2:6:1])      #Start from 2 to 5 and step 1
print(Str1[::2])      #Start from 0 to 10 and step is 2
print(Str1[2::])      #Start from 2 to 10 and step 1
print(Str1[:4:])      #Start from 0 to 4 and step 1
print(Str1[-4:-1])      #Start from -4 to -1 and step is 1
print(Str1[-8:-2:1])      #Start from 8 to -2 and step is one
