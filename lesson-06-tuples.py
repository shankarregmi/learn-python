# Difference  between tuple and list
#    Tuple                                  List
#   Immutable                               Mutable
#   Mostly Heterogenous                     Usually homogenous
#   Accessed thru unpacking or indexing      Access through iteration


example_tuple = 'Hello', 'world', 100  # ('Hello', 'world', 100)
# example_tuple[1] = 'Wolrd' # Error
# del example_tuple[1] # Error also, can't be deleted like list
print(example_tuple[2])  # world


empty = ()  # Empty Tuple
singleton = 'hello',  # Single tuple, note trailing comma


# Unpacking tuple

capitals = 'Kathmandu', 'Berlin', 'Washington'

# print(Nepal, Germany, USA) # Kathmandu Berlin Washington
