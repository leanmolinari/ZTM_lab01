# Exercise: Check for duplicates in list:

some_list = ['a', 'b', 'c', 'd','f', 'g', 'g', 'h','i','i']

duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)