import time

def timer(func):
    def wrapper(*args):
        before = time.time()
        val = func(*args)
        print(f'Function took {time.time() - before} seconds')
        return val
    return wrapper


@timer
def run(seconds):
    time.sleep(seconds)


run(3)
