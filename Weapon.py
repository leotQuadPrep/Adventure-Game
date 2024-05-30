from Object import Object
import GlobalContanor


class Weapon(Object):
    def __init__(self, name, weight, value, durability, damage, affect=None):
        super().__init__(name, weight, value)
        self.durability = durability
        self.damage = damage
        self.affect = affect

    def __str__(self):
        if self.affect:
            return (f"{self.name} weight({self.weight}) value({self.value}) durability({self.durability}) \n"
                    f"damage({self.damage}) affect({self.affect})")
        else:
            return (f"{self.name} weight({self.weight}) value({self.value}) durability({self.durability}) \n"
                    f"damage({self.damage})")

    def attack(self, target):
        target_died = False
        broken = False
        submit_list = [target_died, broken]
        GlobalContanor.action_show_text = ("You attack the "+target.name+" with the "+self.name + ".")
        GlobalContanor.location_changed = True
        self.durability -= 1
        if target.was_attacked(self):
            submit_list[0] = True
        if self.durability == 0:
            submit_list[1] = True
        return submit_list
