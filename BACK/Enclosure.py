class Enclosure:
    def __init__(self, values = []):
        self.id = values[0]
        self.species = values[1]
        self.biome = values[2]
        self.quant = values[3]
        self.keeperId = values[4]
    
    def getSpecies(self):
        return self.species
    def getBiome(self):
        return self.biome
    def getQuant(self):
        return self.quant
    def getKeeperId(self):
        return self.keeperId