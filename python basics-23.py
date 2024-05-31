print(True == 1)
print('' == 1)  # empty  string is said as a falsey
print([] == 1)  # empty array is also said as a falsey
print(10 ==10.0)
print([] == [])
print([1, 2, 3] == [1, 2, 3])
print('1' == 1)  # even it is a false one because it can't be compared in this form 
# equal symbol checks only the equalitybetween the terms

print(True is 1)
print('' is 1) 
print([] is 1) 
print(10 is 10.0)
print([] is []) # this one is false because these lists are different and are in different location and are in different memory space
print([1, 2, 3] is [1, 2, 3]) # this is false because every time the list which we create will be created  under a new location 
print('1' is 1) 

# 'is' checks whether both the terms are in same location and in same memory space
# for exaample the first one should be as print(true is true) so that the result would be true
# this 'is' works on numbers because they are simple types and are in one single location and are in same memory space

a = [1, 2, 3] 
b = [1, 2, 3]
print(a is b) # this will also be false because it applies the same reason which is written as note in line number 15
print(a == b) # this is true because equality only checks the values