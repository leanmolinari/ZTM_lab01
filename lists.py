# Lists

li = [1,2,3,4,5]
li2 = ['a', 'b', 'c']
li3 = [1,2, 3, 'Lean', True]

print(li3[3])
print(li3.count('Lean'))

li.sort(reverse=True)
li2.reverse()

print(li)
print(li2)

new_big_list = list(range(1,100))

print(new_big_list)

# list unpacking

a,b,c, *other = [1,2,3,4,5,6,7,8,9,0]

print(a)
print(b)
print(c)
print(other)

# None

game = None

print(game)