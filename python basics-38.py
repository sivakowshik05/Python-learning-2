# clean code
def is_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0: # or ere we can also code as else:
        return False #                                   return False it also works as like   
    # or we can also code as  return True
    #                         return False just like that in the next line this also works as the same like the previous ones
    # in this case if the line four code is not applicble it directly skips to the next line that is to the line five
print(is_even(50))
print(is_even(51))

def is_even(n1):
    return n1 % 2 == 0

print(is_even(23)) # we can also code like this everything are same
print(is_even(22))