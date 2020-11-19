config = {
    'host': 'localhost',
    'port': 27017,
    'db': 'test',
    'collection': 'testCollection'
}
uri = f'{config["host"]}:{config["port"]}/{config["db"]}/{config["collection"]}'
uri = f'{config.get("host", "localhost")}:{config.get("port", 27017)}'


scores = {
    'Nepal': 100,
    'Germany': 150,
    'USA': 50
}

# for country, score in enumerate(scores): # Enumerate will give indexes as 0, 1
for country, score in scores.items():
    pass
    # print(f'{country:10} : {score:10d}')




# Reading and Writing files

with open('sample.txt', 'a') as sampleFile:
    sampleFile.writelines('\nPython is amazing language')