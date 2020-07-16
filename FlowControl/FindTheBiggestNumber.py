x=int(input("Enter first number : "))
y=int(input("Enter Second number : "))
z=int(input("Enter Third number : "))

if (x>y and x>z):
    big=x;
elif (y>x and y>z):
    big=y;
else:
    big=z;

print(big)