## Python Control Flow

# if statements

x = int(input('Please Enter your age : '))
if type(x) is int:
    if x < 18:
        print('Get lost kiddo')
    elif x == 18:
        print('You still need one more year')
    else:
        print('You are now a grown up Young Man')


# for statements

# simple for loop

for i in range(5): # range(start, end, step)
    print('Shankar Regmi')

# ranged for loop
tensBelow100 = range(10, 101, 10)
for ten in tensBelow100:
    print(ten)

# accesing with index
cars = ['Audi', 'BMW', 'Lamborgini', 'Porsche', 'Bugatti']
for index in range(len(cars)):
    print(index, cars[index])

# break in a for..loop doesn't execute else statement
for num in list(range(1, 10)):
    if num == 5:
        break
    print('Num : ', num)
else:
    print('Finally', num)


# while loop
a = 0
while a <= 100:
    print('Value of a', a)
    a += 10
