#Functio Return Onther function

def first():
    def second():
        print("This is Inner Function")
    return second

x=first()
x()

