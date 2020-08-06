#Access List element using Loop

l1=[10,20,30,40,50]
print(len(l1))

j=0

for i in l1:
    print(i,end=' ')

print()
while j < len(l1):
    print(l1[j] , end=' ')
    j=j+1


