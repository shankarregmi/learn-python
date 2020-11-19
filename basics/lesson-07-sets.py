# A set is an unordered collection with no duplicate elements.

fruits = {'apple', 'orange', 'apple', 'orange'}
# print(fruits) # {'apple', 'orange'},

# membership testing
'mango' in fruits  # False

cars = set()

cars.add('Audi')
cars.add('BMW')
cars.add('Audi')
cars.add('Lamborgini')

# remove duplicates from list using set comprehension

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 7, 3, 4, 1, 1]
unique = {num  for num in my_list}

