# JavaScript Objects
# Key value pairs
# Key should always be string


obj1 = {
    'name': 'Shankar',
    'address': 'Nepal',
    'age': 28
}


list(obj1)  # print keys ['name', 'address', 'age']
obj1.get('name') # Shankar
obj1.keys() # keys
obj1.values() # values

for key, value in obj1.items():
    print('{0} : {1}'.format(key, value))


questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
