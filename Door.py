import GlobalContanor


class Door:
    def __init__(self, open_close, locked_unlocked, direction, door_pair, name, door_type, barrable_unbarrable,
                 barred_unbarred, open_close_str=None):
        self.open_close = open_close
        self.locked_unlocked = locked_unlocked
        self.direction = direction
        self.door_pair = door_pair
        self.name = name
        self.door_type = door_type
        self.open_close_str = open_close_str
        self.barrable_unbarrable = barrable_unbarrable
        self.barred_unbarred = barred_unbarred
        if self.open_close:
            self.open_close_str = "open"
        if not self.open_close_str:
            self.open_close_str = "closed"

    def describe(self):
        if self.door_pair != "":
            if self.direction != "down" and self.direction != "up":
                GlobalContanor.level_show_text += (f". A {self.door_type} leads to the {self.direction}. It is {self.open_close_str}" +
                                                   "")
            else:
                GlobalContanor.level_show_text += (f". A {self.door_type} leads {self.direction}. It is {self.open_close_str}" + "")

    def set_door_pair(self, door):
        self.door_pair = door

    def open(self):
        if self.door_pair != "":
            if self.open_close:
                GlobalContanor.action_show_text = f"The {self.name} is already open."
            elif not self.open_close:
                if self.locked_unlocked and not self.barred_unbarred:
                    GlobalContanor.action_show_text = f"The {self.name} is locked."
                elif self.barred_unbarred and not self.locked_unlocked:
                    GlobalContanor.action_show_text = f"The {self.name} is barred."
                elif self.locked_unlocked and self.barred_unbarred:
                    GlobalContanor.action_show_text = f"The {self.name} is locked and barred."
                elif not self.locked_unlocked and not self.barred_unbarred:
                    GlobalContanor.action_show_text = f"You open the {self.name}."
                    self.open_close = True
                    self.open_close_str = "open"
                    self.door_pair.open_close = True
                    self.door_pair.open_close_str = "open"

    def close(self):
        if self.door_pair != "":
            if not self.open_close:
                GlobalContanor.action_show_text = f"The {self.name} is already closed."
            elif self.open_close:
                GlobalContanor.action_show_text = f"You close the {self.name}."
                self.open_close = False
                self.open_close_str = "closed"
                self.door_pair.open_close = False
                self.door_pair.open_close_str = "closed"

    def unlock(self):
        if self.door_pair != "":
            if self.locked_unlocked:
                GlobalContanor.action_show_text = f"You unlock the {self.name}."
                self.locked_unlocked = False
                self.door_pair.locked_unlocked = False
            elif not self.locked_unlocked:
                GlobalContanor.action_show_text = f"The {self.name} is already unlocked."

    def lock(self):
        if self.door_pair != "":
            if not self.locked_unlocked:
                GlobalContanor.action_show_text = f"You lock the {self.name}."
                self.locked_unlocked = True
                self.door_pair.locked_unlocked = True
            elif self.locked_unlocked:
                GlobalContanor.action_show_text = f"The {self.name} is already locked."

    def bar(self):
        if self.door_pair != "":
            if not self.open_close and self.barrable_unbarrable:
                if not self.barred_unbarred:
                    GlobalContanor.action_show_text = f"You bar the {self.name}."
                    self.barred_unbarred = True
                elif self.barred_unbarred:
                    GlobalContanor.action_show_text = f"The {self.name} is already barred."
            elif self.open_close and self.barrable_unbarrable:
                GlobalContanor.action_show_text = f"You have to close the {self.name} before you bar it."
            elif not self.open_close and not self.barrable_unbarrable:
                GlobalContanor.action_show_text = f"You are on the wrong side of the {self.name} to bar it."
            elif self.open_close and not self.barrable_unbarrable:
                GlobalContanor.action_show_text = (f"You have to go to the other side of the {self.name} and close it before you bar "
                                                   f"it.")

    def unbar(self):
        if self.door_pair != "":
            if not self.barred_unbarred:
                GlobalContanor.action_show_text = f"The {self.name} is already unbarred."
            elif not self.barrable_unbarrable and self.barred_unbarred:
                GlobalContanor.action_show_text = f"You are on the wrong side of the {self.name} to unbar it."
            elif self.barrable_unbarrable and self.barred_unbarred:
                GlobalContanor.action_show_text = f"You unbar the {self.name}."
                self.barred_unbarred = False
                self.door_pair.barred_unbarred = False
