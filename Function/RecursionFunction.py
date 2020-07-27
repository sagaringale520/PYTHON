#Recursion Function

def fact(n):
    if n==0:
        result=1
    else:
        result=n*fact(n-1)
    return result

x=fact(5)

print(x)