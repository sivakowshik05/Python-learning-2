user1 = {
    'basket': [1, 2, 3],
     'greet': 'hello'
}

print(user1.get('age'))

user2 = {
    'basket': [1, 2, 3],
     'greet': 'hello'
}

print(user2.get('age', 55))

user3 = {
    'basket': [1, 2, 3],
     'greet': 'hello',
     'age' : 20
}

print(user3.get('age', 55))

user4 = dict(name = 'BuriBuri')
print(user4)