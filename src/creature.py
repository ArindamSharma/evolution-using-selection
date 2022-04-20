import neuralnetwork as nn
from neurons import *
from genome import Genome
# from world import Coordinates

class Creature:
    def __init__(self,genome:Genome,loc):
        self.coordinates=None
        # self.brain=nn()
        self.genome=genome
        self.age=0
        self.location=loc
        # self.action_neuron=ActionNeurons()
        # self.input_sensor_neuron=Sens()
        # self.inner_neuron=
    
    def grow(self):
        self.age+=1
        pass

    def brainWiring(self):
        pass

    def crossover(self,creature):
        pass

    def getGenome(self)->Genome:
        return self.genome