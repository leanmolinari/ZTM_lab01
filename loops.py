# For loops

user = {
    'name' : 'Jesus',
    'age' : 2021,
    'can_walk_on_wather' : True

}


for key, value in user.items():
    print (key,value)

for k, v in user.items():
    print(k, " : ", v)

for numbers in 50:
    print(numbers)

# while loop


numbers = 0

while numbers < 50:
    print(numbers)
    numbers = numbers + 1
else:
    print('The work is done!')


while True:
    response = input('say something: ')
    if (response == 'bye'):
        break
