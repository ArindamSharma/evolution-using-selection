from pyclbr import Function
from creature import Creature
from genome import Genome
from random import randint,shuffle
from crossover import Crossover
from mutation import Mutation
from selection import Selection

class Evolution():
    def __init__(self,population_size=100,genome_size=4,world_size=128, step_per_gen=300,mutation=0.0):
        self.population_size=population_size
        self.genome_size=genome_size
        self.step_per_gen=step_per_gen
        self.mituation_rate=mutation

        self.world_size=world_size
        self.population=0
        self.unusedLocation=[]
        self.usedLocation={}
        
        self.refreshLocation()
        
    """Adding Population to the World"""
    def introducingPopulation(self,creatureGenomeList:list[Genome]=None):
        if(creatureGenomeList==None):    
            for i in range(self.population_size):
                loc=self.occupyRandomEmptyLocation()
                self.usedLocation[loc]=Creature(Genome(size=self.genome_size),loc)    
        else:
            for creatureGenome in creatureGenomeList:
                loc=self.occupyRandomEmptyLocation()
                self.usedLocation[loc]=Creature(creatureGenome,loc)    

    def grow(self)->None:
        for creature in self.usedLocation:
            self.usedLocation[creature].grow()# to iteratrate once
        # after this loop creature have aged 1 unit
    
    def testGenEvolve(self)->None:
        for gen in range(100):# first 100 generations
            self.refreshLocation()
            self.introducingPopulation()
            
            self.lifecycle()
            # here i have to store the data from genertion 1
            # apply fitness function
            self.terminateUnfit(SelectionCriteria=Selection.selectionCriteria1)
            self.repopulate([i.getGenome() for i in self.usedLocation.values()])

    def terminateUnfit(self,SelectionCriteria:Function)->None:
        '''this function remove the creature which are unfit for the population using fitness function passed '''
        for creature in self.usedLocation:
            if (self.fitnessScore(self.usedLocation[creature],SelectionCriteria)==False):
                del self.usedLocation[creature]

    def repopulate(self,oldcreatures:list[Creature])->None:
        '''this function will re-create creature for the remaining creature based on fitness function'''
        self.refreshLocation()
        x=len(oldcreatures)
        parentAllCombination=[]
        for i in range(x):
            for j in range(i+1,x):
                parentAllCombination.append([i,j])
        newCreatureGenome=[]
        for i in range(self.population_size):
            x=randint(0,len(parentAllCombination))
            tmppair=parentAllCombination.pop(x)
            newCreatureGenome.append(
                Mutation(
                    Crossover(oldcreatures[tmppair[0]].getGenome(),oldcreatures[tmppair[1]],Crossover.SINGLEPOINT,charCrossover=True).offspring,
                    self.mituation_rate,
                    Mutation.RANDOMSWAP
                ).genome
            )
        self.introducingPopulation(newCreatureGenome)
        
    def fitnessScore(self,creature:Creature,fitnessfunction:Function)->bool:
        '''this function return true when the creature fits the selection criteria else false 
        .in other word fitness value 1 is sutable to reproduce and 0 not.'''
        if(fitnessfunction(creature)):
            return True
        return False


    def lifecycle(self):
        '''after this loop creature have finished there lifecycle'''
        for _ in range(self.step_per_gen):
            self.grow()

    def refreshLocation(self)->None:
        '''Clear/Refresh the world '''
        self.unusedLocation.clear()# clearing the world unsued location
        for i in range(self.world_size):
            for j in range(self.world_size):
                self.unusedLocation.append((i,j))
        self.usedLocation.clear()# clearing the used location
        # print("Location Refreshed")

    def getRandomEmptyLocation(self)-> tuple:
        '''This function return any random empty location '''
        upperlimit=(self.world_size*self.world_size)-self.population-1
        self.populationExceedCheck()
        return self.unusedLocation[randint(0,upperlimit)]

    def markLocationAsUsed(self,coordinate:tuple)->tuple:
        self.population+=1
        self.unusedLocation.remove(coordinate)
        return coordinate

    def occupyRandomEmptyLocation(self)->tuple:
        return self.markLocationAsUsed(self.getRandomEmptyLocation())

    def populationExceedCheck(self)->None:
        if(self.population>(self.world_size*self.world_size)):
            raise ValueError("Population Limit Exceed :Max population can be "+str(self.world_size*self.world_size))

if(__name__=="__main__"):
    evo=Evolution(population_size=47,genome_size=4,world_size=10,step_per_gen=300,mutation=0.1)
    print(evo.unusedLocation)
    evo.introducingPopulation()
    print(evo.usedLocation)