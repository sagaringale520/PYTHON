#String Index Method to find pattern

str1="Python is a programming lanaguage"

print(str1.index("program",0,25))

try:
    print(str1.index("Hello",0,25))

except ValueError:
    print("Value Not Found")

except:
    print("Out Of Index error")
