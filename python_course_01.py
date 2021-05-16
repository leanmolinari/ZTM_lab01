# Seeing type
greeting = 'hello world'

print(type(greeting))

# formated strings
greetings_2 = "It\'s a beautiful day right??? \"kind of"

print(greetings_2)

# formmated strings

name = 'Helena'
age = 7

print('Hi {}. you are {} years old'.format(name, age))

print('Hi {1}. you are {0} years old'.format(name, age))

# String index

selfish = 'me me me'
        #  01234567

print(selfish[4])
# [start:stop:stepover]
print(selfish[0:4])


#Immutability

more_numbers = '01234567'
             #  01234567

more_numbers = more_numbers + 'H'

print(more_numbers)

# built-in Functions + Methods

# Function example

print(len('Hello Leandro'))

# Methods example

name = 'Leandro'

print(name.upper())

#booleans
