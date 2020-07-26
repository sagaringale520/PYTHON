#Keyword Argument

def cart(item, price):
    print(item,"cost is :",price)

cart(item=10,price=1000)
cart(price=2000,item=20)

#postional and keyword
cart(30,price=3000)
#cart(item=40,4000)     will give error positional argument after keyword