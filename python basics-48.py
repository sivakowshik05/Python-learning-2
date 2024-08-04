class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

player1 = PlayerCharacter("buriburi", 999)
print(player1.name)
print(player1.age)

player2 = {"name": "buriburi1", "age": 998}
print(player2["name"])
print(player2["age"])