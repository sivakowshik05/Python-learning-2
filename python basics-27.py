for number in range(0, 100):
    print(number)    

for number in range(0, 10):
    print(number)

for number in range(0, 10):
    print(number)

for number in range(0, 10):
    print("email email list") # instead of using "number" we can also use "_" symbol

for _ in range(0, 10):    
    print(_)

for _ in range(0, 10, 2):
    print(_)

for _ in range(0, 10, -1):
    print(_) # this won't work

for _ in range(10, 0, -1):
    print(_) # it counts from backwards

for _ in range(10, 0):
    print(_) # this also won't work

for _ in range(10, 0, -2):
    print(_)

for _ in range(10, 0, -2):
    print(list(range(10)))

for _ in range(2):
    print(list(range(10)))