basket = ['a', 'b', 'c', 'd', 'e']

print(basket.index('d'))
print(basket.index('d', 0))
print(basket.index('d', 0, 4))
print('d' in basket)
print('x' in basket)
print('i' in "my name is Buriburi")

bucket = ['a', 'b', 'c', 'd', 'e', 'd']
print(bucket.count('d'))
print(bucket.count('c'))
bucket.sort()
print(bucket)

blob = ['a', 'b', 'c', 'd', 'e', 'd', 'z']
print(sorted(blob))
new_blob = blob[:] # (or) new_blob = blob.copy
print(new_blob)
print(blob)

buddy = ['a', 'b', 'c', 'd', 'e','d', 'z', 'o']
buddy.reverse()
print(buddy)
buddy.sort()
buddy.reverse()
print(buddy)
print(len(buddy))
print(buddy[::-1]) # again reversed
print(buddy[:])

print(list(range(1, 100))) # starts from 1 and ends with 99
print(list(range(100))) # here it starts from 0 and ends with 99

sentence1 = ''
new_sentence1 = sentence1.join(['hi', 'my', 'name', 'is', 'Buriburi'])
print(new_sentence1)
sentence2 = '!'
new_sentence2 = sentence2.join(['hi', 'my', 'name', 'is', 'Buriburi'])
print(new_sentence2)
sentence3 = ' '
new_sentence3 = sentence3.join(['hi', 'my', 'name', 'is', 'Buriburi'])
print(new_sentence3)

# these can also be written as  new_sentence1 = ''.join(['hi', 'my', 'name', 'is', 'Buriburi'])
# new_sentence2 = '!'.join(['hi', 'my', 'name', 'is', 'Buriburi'])
# new_sentence3 = ' '.join(['hi', 'my', 'name', 'is', 'Buriburi'])

