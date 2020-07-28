#Reduce Function
from functools import reduce

item=[100,200,300,400,500]

total=reduce(lambda x,y:x+y,item)

print(type(total))
print(total)