
class Stack:
    """
    Stack Implementation
    """
    def __init__(self, size):
        print(f'Initialzing new stack with size {size}')
        self.container = list()
        self.size = size
    
    def print(self):
        """
        Print's the element of stack
        """
        container = self.container.copy()
        container.reverse()
        for item in container:
            print(item)

    def push(self, item):
        """
        Push at the top of Stack
        """
        print(f'Adding -> {item}')
        self.container.append(item)
        


# stack = Stack(5)
# stack.push(10)
# stack.push(20)
# stack.push(5)
# stack.print()

class WareHouse:
    purpose = 'storage'
    region = 'west'


WareHouse.purpose = 'retreival'

w1 = WareHouse()
# print('w1.purpose', w1.purpose)

w2 = WareHouse()
w2.purpose = 'storage'
# print('w2.purpose', w2.purpose)
