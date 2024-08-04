class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def run(self):
        return self
    
player1 = PlayerCharacter("buriburi", 999)

print(player1.run())