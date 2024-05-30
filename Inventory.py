import GlobalContanor


class Inventory:
    def __init__(self, strength, items=None, weight=None):
        self.strength = strength
        if items is None:
            items = []
        self.items = items
        if weight is None:
            weight = 0
        self.weight = weight

    def take(self, item):
        self.items.append(item)
        if self.weight + item.weight <= self.strength:
            self.weight = self.weight + item.weight
        else:
            GlobalContanor.level_show_text += f"Your load would be too heavy if you took the {item.name}."

    def drop(self, item):
        found_item = False
        for i in self.items:
            if i.name == item:
                self.items.remove(i)
                found_item = True
                self.weight = self.weight - i.weight
            if found_item:
                return i
        if not found_item:
            GlobalContanor.action_show_text = f"You have no {item} to drop."
            return "no item"

    def item_gone(self, item):
        found_item = False
        for i in self.items:
            if i.name == item:
                self.items.remove(i)
                found_item = True
                self.weight = self.weight - i.weight
            if found_item:
                return i
        if not found_item:
            return "no item"

    def describe(self):
        description = ""
        first_item = True
        for i in self.items:
            if first_item:
                description = description + " " + i.name
                first_item = False
            elif i == self.items[len(self.items)-1] and not first_item:
                description = description + ", and a " + i.name
            else:
                description = description + ", a " + i.name
        if description != "":
            GlobalContanor.action_show_text = f"You have a" + description + "."
        else:
            GlobalContanor.action_show_text = f"You have nothing."
