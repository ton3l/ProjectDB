class Keeper:
    def __init__(self, values = []):
        self.name = values[0]
        self.id = values[1]

    def getId(self):
        return self.id
    def getName(self):
        return self.name