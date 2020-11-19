def add(num1, num2):
    return num1 + num2


# Default argument values

def add10(num1, num2=10):
    return add(num1, num2)


# print(add10(20, 10))
# print(add10(20))


# keyword argument kwargs

def greet(salutation, name='Shankar Regmi', lang='en'):
    if lang == 'de':
        print('Guten Tag {} {}'.format(salutation, name))
    elif lang == 'np':
        print('Namastey {} {}'.format(salutation, name))
    else:
        print('Hello {} {}'.format(salutation, name))

# greet('MR', name='Shankar Remi', lang='np')
# greet('Frau.', 'Prabha Subedi', 'de')


def getDiscount(type, *args, **kwargs):
    print('type ', type)
    for arg in args:
        print('arg ', arg)
    for kw in kwargs:
        print(kw, ":", kwargs[kw])


# getDiscount('Percentage', ['DE', 'NL'], '100%',  value='50%', cap='20')


# Lambda Expressions,
#  use cases : Anonymous callbacks,

def func(num):
    return lambda val: num + val

increment = func(10)

# print(increment(5))  # 15
# print(increment(10))  # 20
# print(increment(20))  # 30

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

doubled = map(lambda num: num * 2, nums)
# print(list(doubled))



# Function Annotations

def greet2(name: str):
    print('Hello {}'.format(name))

greet2('Shankar')
print(greet2.__annotations__)
