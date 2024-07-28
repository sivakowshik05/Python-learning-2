class PlayerCharacter:
    #class object attribute
    membership = True
    def __init__(self, name, age):
        if (PlayerCharacter.membership):
            self.name = name#attributes
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    def run(self, hello):
        print(f'my name is {self.name}')

player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50

print(player1.run('hello'))
print(player2.shout())

#class PlayerCharacter:
#    membership = True
#    def __init__(self, name = 'anonymous', age = 0):
#       if (age > 18):
#          self.name = name
#         self.age = age

#   def shout(self):
#      print(f'my name is {self.name}')
#
#   def run(self, hello):
#      print(f'my name is {self.name}')

#player1 = PlayerCharacter()
#print(player1.run('hello'))
#print(player1.shout()) this code gets an error