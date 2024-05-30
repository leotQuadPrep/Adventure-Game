class Object:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

    def __str__(self):
        return f"{self.name}weight({self.weight})value({self.value})"

    def get_name(self):
        return self.name
