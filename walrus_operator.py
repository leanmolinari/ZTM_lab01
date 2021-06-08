# Walrus Operator

name = 'Leandro Ezequiel Molinari'

if ((n := len(name)) > 5):
    print(F"too long {n} elements")

while ((n := len(name)) > 1):
    print(n)
    name = name[:-1]