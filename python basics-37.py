def test(a):
    print(a)

test('!!!!!!!')

def test(a):
    '''
    info:  this function tests and prints param a
    '''
    print(a)

test('!!!!!!!') 

def test(a):
    '''
    info:  this function tests and prints param a
    '''
    print(a)

test()#-> it is known as the docstring
      # trhis gives the same message which is in the info 
help(test) # we can use help to know what a function does
# or we can code like  print(test.__doc__)
# docstrings are very useful so that we can add comment to a function