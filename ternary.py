# Ternary operator

#condition_if_true if condition else condition_if_else

is_friend = True
can_message = 'message allowed' if is_friend else 'not allowed'

print(can_message)

# Short Circuiting

is_friend2 = True
is_user2 = True

if is_friend2 or is_user2:
    print('best friends for ever')


# Operators

print ('a' > 'A')
print ('a' < 'A')

# Not operator

print(not(True))

# is vs ==
print ('is vs ==')
print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])
# only with is
print ('now with is')
print(True is 1)
print('' is 1)
print([] is 1)
print(10 is 10.0)
print([] is [])
print(True is True)