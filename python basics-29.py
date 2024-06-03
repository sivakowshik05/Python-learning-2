for item in [1, 2, 3]:
    print(item)

i = 0
while i < len([1, 2, 3]):
    print(i)
    i += 1

my_list = [1, 2, 3]
for item in my_list:
    print(item)

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

while True:
    input('say something-1: ')
    break

while True:
   response = input('say something-2: ')
   if(response == 'bye'):
       break