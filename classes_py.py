class Player:
    def __init__(self, name, age: int, level: int):
        self.name = name
        self.age = age
        self.level = level
        self.health = 100 * level
        self.damage = 100 * level

    def __str__(self):  # вывод если делает print(self)
        return 'Player name: {}, age: {}, level: {}'.format(self.name, self.age, self.level)

    def get_data(self):
        print(f"Name: {self.name}, Age: {self.age}, Level: {self.level}, Health: {self.health}, Damage: {self.damage}")


player = Player("sigma", 12, 12)

player.get_data()

print(player)
