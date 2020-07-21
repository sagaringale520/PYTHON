#Number is Positive Or Negative

number=int(input("Enter a Number : "))
ab=abs(number)
print(ab)

if number==ab:
    print("Entered Number is Positive")
else:
    print("Entered Number is Negative")