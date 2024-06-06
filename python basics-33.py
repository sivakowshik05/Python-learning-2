# enumerate is very useful to know the index of the item we are looping through 
for i, char in enumerate('BuriBuri'):
    print(i, char) # i - index ; index of each character ;; char - character
  
for i, char in enumerate([1, 2, 3]):
    print(i, char) # here it shows the index of the items in the list 

for i, char in enumerate((1, 2, 3)):
    print(i, char) 

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f'index of 50 is: {i}')

for i, char in enumerate(list(range(100))):
    print(i, char)