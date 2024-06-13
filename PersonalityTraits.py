class PersonalityTraits:
    def __init__(self, trait_max, trait_goal, trait_base_decrease_speed, trait_value, trait_importance):
        self.trait_max = trait_max * trait_importance
        self.trait_goal = trait_goal * trait_importance
        self.trait_base_decrease_speed = trait_base_decrease_speed * trait_importance
        self.trait_value = trait_value * trait_importance
        self.trait_importance = trait_importance

    def exist(self):
        self.trait_value = self.trait_value-self.trait_base_decrease_speed
