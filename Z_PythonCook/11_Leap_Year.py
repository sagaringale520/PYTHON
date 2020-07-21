#Leap Year

year=2020

if year %100 ==0 and year%400==0:
    print("2020 is leap Year")
elif year%4==0:
    print("2020 is leap Year")
else:
    print("2020 is not a leap year")