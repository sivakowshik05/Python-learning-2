my_set = {1, 2, 3, 4, 5}
print(my_set)
my_set2= {1, 2, 3, 4, 5, 5}
print(my_set2)
my_set3 = {1, 2, 3, 4, 5, 5}
my_set3.add(100)
my_set3.add(2)
print(my_set3)
my_list = [1, 2, 3, 4, 5, 5]
print(set(my_list))
print(5 in my_set)
print(len(my_set))
print(list(my_set))
new_set = my_set.copy()
my_set.clear()
print(new_set)
print(my_set)