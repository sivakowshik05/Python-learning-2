is_old = True
is_licenced = True

if is_old:
    print('you are old enough to drive!')
elif is_licenced:
    print('you can drive now')
else:
    print('you are not enough old to drive!')
print('okoko')  # without and
is_old2 = True
is_licenced2 = True

if is_old2 and is_licenced2:
    print('you are old enough to drive, and you have a licence')
else:
    print('you are not enough old to drive!')
print('okoko')