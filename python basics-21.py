# short circuiting
is_friend1 = True
is_user1 = True

if is_friend1 and is_user1:
    print('best friends forever')

is_friend2 = True
is_user2 = False

if is_friend2 or is_user2:
    print('best friends forever')    

is_friend3 = True
is_user3 = False

if True or False:
    print('best friends forever')