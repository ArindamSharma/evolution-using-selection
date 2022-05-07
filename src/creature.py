# import neuralnetwork as nn
# from neurons import SensorNeuron,ActionNeuron,InnerNeuron,Connection,Weight
from genome import Genome
from encode import Encode,Decode
from random import randint
from neuralnet import NeuralNet

class Creature:
    envLoc={}
    direction={
        0:"N",
        1:"NE",
        2:"E",
        3:"EW",
        4:"W",
        5:"WS",
        6:"S",
        7:"SE",
    }
    def resetEnvLoc()->None:
        '''Clears out the Locations of Creature'''
        Creature.envLoc.clear()

    def __init__(self,genome:Genome,location:tuple,inner_neuron:int=1):
        '''Takes Genome for creation of Creature and Location where it exist and other Creatures Location Pointer'''
        Creature.envLoc[location]=self
        self.genome=genome
        self.brain=NeuralNet(Decode(self.genome).linkArray)
        self.age=0
        self.location=location
        self.birthloc=location
        self.current_direction=randint(0,7)
    
    def grow(self):
        self.age+=1
        pass

    def brainWiring(self):
        pass

    def crossover(self,creature):
        pass

    def getGenome(self)->Genome:
        return Encode(self.brain.linkArray).genome

if __name__=="__main__":
    a=Creature(Genome(size=4),(4,3),3)
    print(a.brain)