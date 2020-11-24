# They are written like regular functions but use the 'yield' statement whenever they want to return data.
# Each time next() is called on it, the generator resumes where it left off
# (it remembers all the data values and which statement was last executed)


users = ['John', 'Bob', 'Ram', 'Hari', 'Shyam']

index = 0
def test():
    nonlocal index
    yield users[index]
    index = index + 1

print(list(test()))
print(list(test()))
print(list(test()))
# def reverse(data):
#     for index in range(len(data)-1, -1, -1):
#         yield data[index]


# reversed = reverse(users)

# print(list(reversed)) # reversed list

