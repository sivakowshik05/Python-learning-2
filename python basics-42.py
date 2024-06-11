a = 1

def confusion():
    a = 5
    return a

print(a)
print(confusion())

a = 1

def parent():
    a = 10
    def confusion():
        return a
    return confusion()

print(parent())
print(a)

a = 1

def parent():
    def confusion():
        return a
    return confusion()

print(parent())
print(a) # here global rule is applied by the python interpreter

a = 1

def parent():
    def confusion():
        return sum
    return confusion()

print(parent())
print(a) # here the 4th order will be applied that is it checks whether the sum is a python built in function

# scope order
#1 - start with local , here a = 5 is the localscope
#2 check whether there is a parent local?
#3 - global rule
#4 - built in python funtion , this is a tricky one
