import GlobalContanor


class Creature:
    def __init__(self, name, weight, drops, health, value, hunger=None, thirst=None, safety=None, bored=None, social=None, personality=None, location=""):
        self.name = name
        self.weight = weight
        self.drops = drops
        self.health = health
        self.value = value
        self.location = location
        self.hunger = hunger
        self.thirst = thirst
        self.safety = safety
        self.bored = bored
        self.social = social
        self.personality = personality

    def __str__(self):
        return f"{self.name} {self.weight} {self.drops} {self.health} {self.value}"

    def was_attacked(self, weapon):
        self.health = self.health-weapon.damage
        if self.health <= 0:
            GlobalContanor.action_show_text = ("The " + self.name + " dies.")
            GlobalContanor.location_changed = True
            self.location = ""
            del self
            return True

    def get_name(self):
        return self.name

    def set_location(self, level):
        self.location = level

    def act(self):
        action_list = self.location.actions
        action = self.personality.evaluate(action_list)
