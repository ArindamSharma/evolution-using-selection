import random
from creature import Creature
from genome import Genome

class Evolution():
    def __init__(self,population_size=100,genome_size=4,world_size=128, step_per_gen=300,mutation=0.0):
        self.population_size=population_size
        self.genome_size=genome_size
        self.world_size=world_size
        self.step_per_gen=step_per_gen
        self.mituation_rate=mutation
        
        self.location_array=[]
        self.population_array=[]


    """ initializing creatures"""
    def initCreature(self):
        # all possible locations
        for x in range(self.world_size):
            for y in range(self.world_size):
                self.location_array.append((x,y))
        # print(location_array)
        
    """Adding Population to the World"""
    def introducingPopulation(self):
        for i in range(self.population_size):
            loc=self.location_array.pop(random.randint(0,self.world_size*self.world_size-1))
            self.population_array.append(Creature(Genome(size=self.genome_size),loc))

    def grow(self):
        for creature in self.population_array:
            creature.grow()# to iteratrate once
        # after this loop creature have aged 1 unit

    def lifecycle(self):
        for _ in range(self.step_per_gen):
            self.grow()
        # after this loop creature have finished there lifecycle
        
        # here i have to store the data from genertion 1
        # apply fitness function

if(__name__=="__main__"):
    evo=Evolution()