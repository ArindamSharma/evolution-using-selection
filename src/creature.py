from neuralnet import NeuralNet
import neuralnetwork as nn
from neurons import *
from genome import Genome
from encode import Encode,Decode

class Creature:
    envLoc={}
    def resetEnvLoc()->None:
        '''Clears out the Locations of Creature'''
        Creature.envLoc.clear()

    def __init__(self,genome:Genome,location:tuple,inner_neuron:int=1):
        '''Takes Genome for creation of Creature and Location where it exist and other Creatures Location Pointer'''
        Creature.envLoc[location]=self
        self.genome=genome
        self.brain=NeuralNet(Decode(self.genome).linkArray,inner_neuron)
        self.age=0
        self.location=location
        self.birthloc=location
    
    def grow(self):
        self.age+=1
        pass

    def brainWiring(self):
        pass

    def crossover(self,creature):
        pass

    def getGenome(self)->Genome:
        return Encode(self.brain).genome

if __name__=="__main__":
    a=Creature(Genome(size=4),(4,3),3)
    # print(a.brain)