import GlobalContanor


class Personality:
    def __init__(self, traits, optimal_action=None, available_actions=None, satisfied=None):
        self.traits = traits
        if optimal_action is None:
            optimal_action = ""
        self.optimal_action = optimal_action
        if available_actions is None:
            available_actions = []
        self.available_actions = available_actions
        if satisfied is None:
            satisfied = 0
        self.satisfied = satisfied

    def evaluate(self, actions):
        self.available_actions = actions
        global potential_optimal_action
        global potential_optimal_satisfied
        potential_optimal_action = []
        potential_optimal_satisfied = 100000
        for action in self.available_actions:
            global potential_satisfied
            potential_satisfied = 0
            traits_value = []
            traits_goal = []
            for i in self.traits:
                traits_value.append(i.trait_value)
                traits_goal.append(i.trait_goal)
            traits_value[action[0]] += action[1]
            i = 0
            while i < len(traits_value):
                if traits_value[i] < traits_goal[i]:
                    potential_satisfied += traits_goal[i] - traits_value[i]
                if traits_value[i] > traits_goal[i]:
                    potential_satisfied += traits_value[i] - traits_goal[i]
                i += 1
            if potential_satisfied < potential_optimal_satisfied:
                potential_optimal_satisfied = potential_satisfied
                potential_optimal_action = action
        self.optimal_action = potential_optimal_action
        return self.optimal_action
