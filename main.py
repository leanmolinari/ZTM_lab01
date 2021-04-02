#First program
name = input('What is your name?: ')
print ('Hola como estas? ' + name + '!!!')

#Fundamental Data types
int
float
bool
str
list
tuple
set
dict

#Classes --> Custom types

#Specialized Data Types


#Strings

#example of long strings

long_string  = '''
WWWWWWW
--   --
O     O
  \/
------
'''

print (long_string)

#Type conversion

print(type(str(100)))

#Escape Sequence "\"

weather = 'It\'s \"kind" of sunny'

print (weather)

#Formatted strings .format {}

name = 'Helena'
age = 7

print('Hi {}!!. you are beautiful and you are {}'.format(name, age))

print ('Hola {name}!!! como estas?? tenes {age} '.format(name='lean', age=39))

#string index

selfish = 'me me me'
          #01234567
print(selfish[4]) 

#[start:stop]
print(selfish[0:4])

some_numbers = '01234567890'
#[start:stop:stepover]
print(some_numbers[0:9:2]) 
