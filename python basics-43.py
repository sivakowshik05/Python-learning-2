a = 10
def confusion(b):
    print(b)
    a = 90

confusion(300)

total = 0

def count():
    total = 0
    total += 1
    return total

print(count) # result will be 1 if we run the code

total = 0

def count():
    global total
    total += 1
    return total

count()
count()
print(count) # result will be 3 if we run the code

# or

total = 0

def count(total):
    total += 1
    return total

print(count(count(count(total))))