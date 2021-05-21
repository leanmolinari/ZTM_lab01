# Dictionary (data structure)
# dict 

dictionary = {
    'a' : 1,
    'b' : 2,
    'c' : 3
 }

print(dictionary['b'])

new_dic = {
    'a' : [1,2,3,4,5],
    'b' : True,
    'c' : [1,[2,3,4],5]
}

print(new_dic['c'][1])
print(new_dic.items())

# when use a list or when use a dictionary
# List is order.
# dictionary is not order.
    #dictionary can have diferents data types like a key but is not possible set a list like a key of dictionary.

# dictionary methods
# another way for define a dictionary and is using "dict"

new_dic2 = dict(name ='leandro')

print(new_dic2)
