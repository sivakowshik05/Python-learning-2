# iterable - it can be list, dictionary, tuple, set, string
# iterate - it means one by one to check each item in the collection
user = {
    'name': 'BuriBuri',
    'age': 5006,
    'can_swim': False
}

for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item) # now we will be ab;le to iterate the keys

for item in user.items():
    key, value = item;
    print(key, value) # or we  can also make it in this form
                      # for key, value in user.items():
                      # print(key, value)
  