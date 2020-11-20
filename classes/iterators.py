# Behind the scenes, the for statement calls iter() on the container object.
# The function returns an iterator object that defines the method __next__()
# which accesses elements in the container one at a time.
# When there are no more elements, __next__() raises a StopIteration exception
# which tells the for loop to terminate.
# You can call the __next__() method using the next() built-in function
# this example shows how it all works:

users = ['John', 'Bob', 'Ram', 'Hari', 'Shyam']

# it = iter(users)

# try:
#     while True:
#         print(next(it))
# except StopIteration as e:
#     print('Done iterating')


class Reverse:
    """Iterator for looping over a sequence backwards."""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        print('next called')
        # if self.index == 0:
        #     raise StopIteration
        # self.index = self.index - 1
        # return self.data[self.index]


rev = Reverse(users)

it = iter(rev)

try:
    while True:
        print(next(it))
except StopIteration as e:
    print('Done iterating')
