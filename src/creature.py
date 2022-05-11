# import neuralnetwork as nn
# from neurons import SensorNeuron,ActionNeuron,InnerNeuron,Connection,Weight
# from neuralnet import NeuralNet
from encode import Encode,Decode
from random import randint
from neuralnetworkv2 import NeuralNetwork
from coordinate import Coordinate
from compass import Compass

class Creature:
    envLoc:list=[]
    
    def resetEnvLoc()->None:
        '''Clears out the Locations of Creature'''
        Creature.envLoc.clear()

    def __init__(self,genome,location:Coordinate,simparam):
        '''Takes Genome for creation of Creature and Location where it exist and other Creatures Location Pointer'''
        self.id=len(Creature.envLoc)
        Creature.envLoc.append(self)
        self.genome=genome
        self.age=0
        self.location=location
        self.birthloc=location
        self.direction=Compass()
        self.lastmovex=None
        self.lastmovey=None

        self.r=None
        self.g=None
        self.b=None
        # self.brain=NeuralNet(Decode(self.genome).linkArray)
        self.brain=NeuralNetwork(self,Decode(self.genome).linkArray,simparam)
        # print(self.r,self.g,self.b)
    
    def grow(self):
        self.brain.feedForward()
        # print(len(self.envLoc))

    def crossover(self,creature):
        pass

    def getGenome(self)->None:
        '''Updating neural network adjacency list and extracting genome'''
        self.brain.updateWeight()
        return Encode(self.brain.getConnectionList()).genome

    def __str__(self) -> str:
        tmp="Age:" + str(self.age)+"\n"
        tmp="ID:" + str(self.id)+"\n"
        tmp+=str(self.location)+"\n"
        tmp+="Genome: " + str(self.genome)+"\n"
        tmp+= str(self.direction)+"\n"
        return tmp
    def __repr__(self) -> str:
        return str(self.location)

if __name__=="__main__":
    from genome import Genome
    from evolution import Evolution
    # tmp_genome="1c994da65b92775ae59e2194f12ba069"
    # print(tmp_genome)
    x=Evolution()
    a=Creature(Genome(size=4),Coordinate(4,3),x)
    b=Creature(Genome(size=4),Coordinate(40,30),x)
    print(Creature.envLoc)
    print("-----------------------------")
    print(a)
    # print(a.brain.linklist)
    print(a.brain.sensor)
    print(a.brain.inner)
    print(a.brain.action)
    print()
    print(b)
    print(b.brain.sensor)
    print(b.brain.inner)
    print(b.brain.action)
    print("-----------------------------")
    
    
    print("------------Feed Forward Starts----------------")
    # a.grow()
    for _ in range(100):
        a.brain.feedForward()
        b.brain.feedForward()
    # print(a.brain.updateWeight())
    # print(a.brain.linklist)
    print("------------Feed Forward ends----------------")
    
    print("-----------------------------")
    print(a)
    # print(a.brain.linklist)
    print(a.brain.sensor)
    print(a.brain.inner)
    print(a.brain.action)
    print()
    print(b)
    print(b.brain.sensor)
    print(b.brain.inner)
    print(b.brain.action)
    print("-----------------------------")