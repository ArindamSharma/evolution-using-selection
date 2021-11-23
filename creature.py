import neuralnetwork as nn
class Creature:
    def __init__(self,genome_length):
        self.coordinates=None
        self.brain=nn()
        self.genome_length=genome_length
        self.genome=None
        