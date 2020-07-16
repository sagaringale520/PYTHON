#Search a element in List

l=[10,20,30,40,50]

search=int(input("Enter the search number : "))

for i in l:
    if i==search:
        print("Number Found")
        break
else:
    print("Number Not Found")