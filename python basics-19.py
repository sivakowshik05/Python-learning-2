is_old = bool('hello')
is_licenced = bool(5)

print(bool('hello'))
print(bool(5))

# Truthy value 

if is_old and is_licenced:
    print('you are old enough to drive, and you have a licence!')
else:
    print('you are not of age!')

print('okok')

is_old2 = bool('')
is_licenced2 = bool(0)

print(bool(''))
print(bool(0))

# Falsy value

if is_old2 and is_licenced2:
    print('you are old enough to drive, and you have a licence!')
else:
    print('you are not of age!')

print('okok')

password = '123'
username = 'buriburi'

# Truthy and Falsy

if password and username:
    print('something')

else:
    print('do something')

print('okok')    