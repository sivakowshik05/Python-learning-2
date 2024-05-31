for item in 'BuriBuri Stores':
    print(item)
for item in [1, 2, 3, 4, 5]:
    print(item) # this can also be applied in lists
for item in {1, 2, 3, 4, 5}:
    print(item) # this can also be applied in sets
for item in (1, 2, 3, 4, 5):
    print(item) # this can also be applied in tuples
    print(item)
    print(item) # now it each thing will be printed twice
print(item) # now, here only five will be printed four times because the value of item is the last thing in the list that is here the value of item is five so five will be printed four times
print('hi!') # the hi! will be printed once atlast because it is not in the list
for item in (1, 2, 3, 4, 5):
    for x in ['a', 'b', 'c']:
        print(item, x) # nested loops will be created