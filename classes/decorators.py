import time


def logger(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        print('Starting function call')
        val = func(*args, **kwargs)
        print(f'Function took {time.time() - before} seconds')
        return val
    return wrapper


@logger
def greet(name):
    print(f'Hello !! {name}')


greet('Shankar')
