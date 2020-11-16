from sys import argv

# Strings


def strings():
    str = 'Shankar Regmi'
    print('length of string', len(str))

    print('first character :', str[0])  # S
    print('last character :', str[-1])  # i

    # Slicing
    print('from first -> 7 str[0:7] :', str[0:7])  # Shankar
    print('Until 7 str[:7] :', str[:7])  # Shankar
    print('from 9 -> Last str[8:] :', str[8:])  # Regmi
    print('Last 5 character [-5:] :', str[-5:])


# List  (Arrays in JS)
def lists():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    copy = letters[:]  # shallow copy
    copy[2] = 'B'  # list are mutable unlike strings
    # print('shallow copy with modified value', copy)

    # concatenate
    result = letters + ['h', 'i', 'j']
    # print('concatenated result', result)

    # adding at the end of list
    result.append('k')
    print(result)

    # replacing using slicing
    letters[2:5] = ['C', 'D', 'E']
    print('After modification', letters)

    # removing
    letters[2:5] = []
    print('After removing', letters)


# Test
if __name__ == '__main__':
    if len(argv) == 2 and argv[1]:
        try:
            eval('{}()'.format(argv[1]))
        except NameError:
            print('No Function Definition found')
    else:
        print('Please specify function')
