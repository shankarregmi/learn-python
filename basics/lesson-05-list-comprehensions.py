# List Comprehensions
nums = [num for num in range(10, 101, 10)]
less_than_50 = [num for num in nums if num < 50]
halves = [num // 2 for num in nums]  # divided all by 2

squares = [x**2 for x in range(10)]
# print(squares)

names = [(name, surname) for name in ['Shankar', 'Prabha', 'Sandesh']
         for surname in ['Regmi', 'Subedi', 'Sharma']]

fruits = [
    {'name': 'Apple', 'rank': 5},
    {'name': 'Banana', 'rank': 6},
    {'name': 'Orange', 'rank': 8},
    {'name': 'Mango', 'rank': 9},
    {'name': 'Kiwi', 'rank': 10},
]

best_fruit = [f['name'] for f in fruits if f['rank'] > 5]


