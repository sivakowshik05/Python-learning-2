selfish = "01234567"
        #  01234567

# [start:stop:sepover] 
print(selfish[4])
print(selfish[2:6])
print(selfish[0:5:3])
print(selfish[1:]) #[1:]-starts from one and stops when nothing is there
print(selfish[:5]) #[:5]-starts from zero and ends with four
print(selfish[::1])#[::1]-it directly stepovers by one when nothing is there before
print(selfish[-1]) #[-1]it starts from back
print(selfish[::-1])#[::-1]it stepovers from back