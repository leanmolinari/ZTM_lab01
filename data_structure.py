# Data Strcture

# lists
li = [1,2,3,4,5]
li2 = ['a','b','c']
li3 = [1,2,2.5,'a','b',True]

print(li3[3])

# List slicing

amazon_cart = [
  'notebooks',
  'sunglases',
  'iphone',
  'grape'
]

amazon_cart[0] = 'Macbook Pro'
print(amazon_cart[0::2])
print(amazon_cart)

# Matrix

matrix = [
  [1,2,3],
  [2,4,5],
  ['a','b','c'],
  [1,[2,3,4],5]
]

print(matrix)
print(type(matrix))
print (matrix[2][2])