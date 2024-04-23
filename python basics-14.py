user = {
    'basket': [1, 2, 3],
     'greet': 'hello',
     'age' : 20
}

print('basket' in user)
print('size' in user)
print('age' in user.keys()) # keys simply checks the keys
print('hello' in user.items())
print(user.items())
print(user.clear()) # or user.clear
                    # print(user)
                    # the result will be none
                    
user2 = user.copy()
print(user)
print(user2)
print(user.clear)
print(user2)
print(user.pop('age'))
print(user) # here age does not exist anymore
print(user.popitem()) # here it randomly pops of something that is both value and key
print(user)
print(user.update({'ages': 55}))
print(user)
