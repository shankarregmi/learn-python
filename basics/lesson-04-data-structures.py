# List
companies = ['Google', 'Facebook', 'Microsoft', 'Amazon']

companies.append('Apple')  # companies[len(companies):] = ['Apple']
companies.extend(['LinkedIn', 'GitHub'])
companies.insert(4, 'Siemens')  # After Amazon

companies.remove('Siemens')  # Raises Exception if no matching element found

# print('popped', companies.pop(len(companies) - 1)) # Github is popped
# print(companies.index('Amazon')) # 3
# companies.clear() # flush all elements

companies.sort()  # sorts in place,
# print(companies) # prints sorted companies ['Amazon', 'Apple', 'Facebook', 'GitHub', 'Google', 'LinkedIn', 'Microsoft']
companies.reverse()  # reverse sorted list
# print(companies) # prints reverse sorted companies ['Microsoft', 'LinkedIn', 'Google', 'GitHub', 'Facebook', 'Apple', 'Amazon']


# List as stack

stack = []
stack.append(1)
stack.append(2)
stack.append(3)

print(stack.pop())  # 3
print(stack.pop())  # 2
print(stack.pop())  # 1
print(stack) # []
# print(stack.pop()) # Error Empty Stack
