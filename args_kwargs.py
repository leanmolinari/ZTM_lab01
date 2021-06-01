# *args **kwargs

def sueper_function(*args, **kwargs):
    total = 0
    print (args)
    print (kwargs)
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(sueper_function(1,2,3,4,5, num1=5, num2= 10))


