# arguments and key word arguments
# *args - *arguments
# **kwargs - **keywordarguments
# func - fuction

def super_func(*args): # * this symbol accepts any numbers in the positional arguments
    print(*args) # here now we get the parameters that are in the tuple  if we remove the star we get the tuple in which the parameters are situated
    print(args)
    return sum(args)

print(super_func(1, 2, 3, 4, 5)) # this is the place where we have a positional arguments

def super_func(*args, **kwargs):
    print(kwargs)
    return sum(args)

print(super_func(1, 2, 3, 4, 5, num1 = 5, num2 = 10)) # now if we print it we can get a dictionary

def super_func(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total  # now here so that the sum() would be as the total

print(super_func(1, 2, 3, 4, 5, num1 = 5, num2 = 10))

# Rule : here first we have our params that is the parameters then we have our * args that is the arguments then we have our default parameters and then atlast we have our **kwargs that is our keyword arguments
# default parameters comes after *args(arguments) but before **kwargs(keyword arguments)

def super_func(name, *args, i = 'hi', **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func('BuriBuri', 1, 2, 3, 4, 5, num1 = 5, num2 = 10)) # now we have everything which are in the
# but usually we will be using only *args(aguments) and **kwargs(keyword arguments)
# and the name is the params print(super_func('BuriBuri', 1, 2, 3, 4, 5, num1 = 5, num2 = 10)) her when we run the code both the name and the DP(default parameters) won't work and it is not compulsory to add DP and name in the code because it won't be included in anything
# in this code we followed the rule.