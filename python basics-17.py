my_set = {1, 2, 3, 4, 5}
BuriBuri_set = {4, 5, 6, 7, 8, 9, 0}
print(my_set.difference(BuriBuri_set))
print(my_set.discard(5))
print(my_set) 
print(my_set.difference_update(BuriBuri_set))
print(my_set)
print(my_set.intersection(BuriBuri_set))
print(my_set)
my_set2 = {1, 2, 3}
print(my_set2.isdisjoint(BuriBuri_set)) # this states whether the values are uncommon in each sets by using booleans
print(my_set.union(BuriBuri_set)) # the values get merged
print(my_set | BuriBuri_set) # this line can also be used to merge the values
print(my_set & BuriBuri_set) # this can also be done for the intersection purpose
my_set3 = {4, 5}
print(my_set3.issubset(BuriBuri_set))
print(my_set.issubset(BuriBuri_set))
print(BuriBuri_set.issuperset(my_set3)) # it show whether the values of buriburi_set in my_set by usin booleans
print(BuriBuri_set.issuperset(my_set))
