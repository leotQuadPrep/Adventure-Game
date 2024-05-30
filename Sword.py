from Weapon import Weapon


class Sword(Weapon):
    def __init__(self, name, weight, value, durability, damage, affect=None):
        super().__init__(name, weight, value, durability, damage, affect)
