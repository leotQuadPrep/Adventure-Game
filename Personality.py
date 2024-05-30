import GlobalContanor


class Personality:
    def __init__(self, traits, optimal_action=None, available_actions=None):
        self.traits = traits
        if optimal_action is None:
            optimal_action = ""
        self.optimal_action = optimal_action
        if available_actions is None:
            available_actions = []
        self.available_actions = available_actions

    def evaluate(self):
        action_bonus_index = 0
        for action in self.available_actions:
            for action_bonus in action:
                i=1