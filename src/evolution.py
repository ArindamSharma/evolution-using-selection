from creature import Creature
from genome import Genome
from random import randint,shuffle
from crossover import Crossover
from mutation import Mutation
from coordinate import Coordinate
from connection import ConnectionArray,Connection

class Evolution():
    def __init__(self,population_size=100,genome_size=4,world_size=128, step_per_gen=300,mutation=0.0,inner_neuron=1,max_generation=100):
        
        self.max_generation=max_generation
        self.world_size=world_size
        self.population_size=population_size
        self.step_per_gen=step_per_gen
        self.genome_size=genome_size
        self.mutation_rate=mutation
        self.inner_neuron=inner_neuron
        
        self.population=0
        self.unusedLocation:list[Coordinate]=[]

        self.survival_rate=None
        self.diversity=None
        self.murder=None

        self.refreshLocation()
        
    """Adding Population to the World"""
    def introducingPopulation(self,creatureGenomeList:list[Genome]=None):
        if(creatureGenomeList==None):    
            for i in range(self.population_size):
                loc=self.occupyRandomEmptyLocation()
                # self.usedLocation[loc]=Creature(Genome(size=self.genome_size),loc,self.simparam)    
                Creature(Genome(size=self.genome_size),loc,self)    
        else:
            for creatureGenome in creatureGenomeList:
                loc=self.occupyRandomEmptyLocation()
                # self.usedLocation[loc]=Creature(creatureGenome,loc,self.simparam)    
                Creature(creatureGenome,loc,self)    

    def grow(self)->None:
        ''' after this loop creature have aged 1 unit'''
        for creature in Creature.envLoc:
            creature.grow()# to iteratrate once
    
    def terminateUnfit(self,SelectionCriteria:any)->None:
        '''this function remove the creature which are unfit for the population using fitness function passed '''
        creatureToRemove=[]
        for creature in Creature.envLoc:
            if (self.fitnessScore(creature,SelectionCriteria)==False):
                creatureToRemove.append(creature)

        self.survival_rate=(self.population_size-len(creatureToRemove))/self.population_size
        self.survival_rate*=100
        print("Survivers :",self.survival_rate,"%")
        # print("Creature to delete",len(creatureToRemove))
        for creature in creatureToRemove:
            Creature.envLoc.remove(creature)

    def repopulate(self,oldCreaturesGenomeList:list[Genome])->list[Genome]:
        '''this function will re-create creature for the remaining creature genome based on fitness function and return new Creatures Genome List'''
        if(len(oldCreaturesGenomeList)==0):
            raise Exception("passed population cannot be empty")
        
        self.refreshLocation()
        x=len(oldCreaturesGenomeList)
        parentAllCombination=[]
        for i in range(x):
            for j in range(i+1,x):
                parentAllCombination.append([i,j])
        
        newCreatureGenomeList=[]
        for i in range(self.population_size):
            x=randint(0,len(parentAllCombination)-1)
            tmppair=parentAllCombination.pop(x)
            # print(oldCreaturesGenomeList[tmppair[0]],oldCreaturesGenomeList[tmppair[1]],Crossover(oldCreaturesGenomeList[tmppair[0]],oldCreaturesGenomeList[tmppair[1]],Crossover.SINGLEPOINT,geneCrossover=True).offspring,Mutation(Crossover(oldCreaturesGenomeList[tmppair[0]],oldCreaturesGenomeList[tmppair[1]],Crossover.SINGLEPOINT,charCrossover=True).offspring,self.mituation_rate,Mutation.RANDOMSWAP).genome,)
            newCreatureGenomeList.append(Mutation(Crossover(oldCreaturesGenomeList[tmppair[0]],oldCreaturesGenomeList[tmppair[1]],Crossover.SINGLEPOINT,geneCrossover=True).offspring,self.mutation_rate,Mutation.RANDOMSWAP).genome)
        # print(newCreatureGenomeList)
        return newCreatureGenomeList
        # self.introducingPopulation(newCreatureGenomeList)
        
    def fitnessScore(self,creature:Creature,fitnessfunction:any)->bool:
        '''this function return true when the creature fits the selection criteria else false 
        .in other word fitness value 1 is sutable to reproduce and 0 not.'''
        if(fitnessfunction(creature)):
            return True
        return False

    def lifecycle(self,gencount:int):
        '''after this loop creature have finished there lifecycle'''
        # print()
        for _ in range(self.step_per_gen):
            print("Gen",gencount,"- Day",_+1,end="\r")
            self.grow()
    
    def storeGenData(self)->None:
        '''will store the date/genome string into a file'''
        pass

    def refreshLocation(self)->None:
        '''Clear/Refresh the world '''
        Creature.resetEnvLoc()
        self.unusedLocation.clear()# clearing the world unsued location
        for i in range(self.world_size):
            for j in range(self.world_size):
                self.unusedLocation.append(Coordinate(i,j))
        # self.usedLocation.clear()# clearing the used location
        self.population=0
        # print("Location Refreshed")

    def getRandomEmptyLocation(self)-> Coordinate:
        '''This function return any random empty location '''
        upperlimit=(self.world_size*self.world_size)-self.population-1
        self.populationExceedCheck()
        return self.unusedLocation[randint(0,upperlimit)]

    def markLocationAsUsed(self,coordinate:Coordinate)->Coordinate:
        self.population+=1
        self.unusedLocation.remove(coordinate)
        return coordinate

    def occupyRandomEmptyLocation(self)->Coordinate:
        return self.markLocationAsUsed(self.getRandomEmptyLocation())

    def populationExceedCheck(self)->None:
        if(self.population>(self.world_size*self.world_size)):
            raise ValueError("Population Limit Exceed :Max population can be "+str(self.world_size*self.world_size))
    
    def testGenEvolve(self,gen_limit=1)->None:
        population=[Genome(size=self.genome_size) for i in range(self.population_size)]
        for gen in range(gen_limit+1):# first 100 generations
            self.refreshLocation()
            # print(population)
            self.introducingPopulation(population)
            self.lifecycle(gen)
            # here i have to store the data from genertion 1
            self.storeGenData()
            # apply fitness function
            # print(self.usedLocation,[i.getGenome() for i in self.usedLocation.values()])
            self.terminateUnfit(SelectionCriteria=self.selectionCriteria1)
            # print(self.usedLocation,[i.getGenome() for i in self.usedLocation.values()])
            population=self.repopulate([i.getGenome() for i in Creature.envLoc])
        print()

    def selectionCriteria1(self,creature:Creature)->bool:
        '''this is custom function thats changes with different criteria'''
        # return True
        if(creature.location.x>self.world_size/2):
            return True
        return False

    def selectionCriteria2(self,creature:Creature)->bool:
        '''this is custom function thats changes with different criteria'''
        # return True
        if(creature.location.y>self.world_size/2):
            # print(True)
            return True
        # print(False)
        return False

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return "============ Parameters ========\n"\
        +" Max Geneneration :".ljust(21," ")+str(self.max_generation).rjust(9," ")+"\n"\
        +" World Size :".ljust(21," ")+str(self.world_size).rjust(9," ")+"\n"\
        +" Population :".ljust(21," ")+str(self.population_size).rjust(9," ")+"\n"\
        +" Step Per Generation :".ljust(21," ")+str(self.step_per_gen).rjust(9," ")+"\n"\
        +" Genome Size :".ljust(21," ")+str(self.genome_size).rjust(9," ")+"\n"\
        +" Mutation Rate :".ljust(21," ")+str(self.mutation_rate).rjust(9," ")+"\n"\
        +" Mutation Rate :".ljust(21," ")+str(self.inner_neuron).rjust(9," ")+"\n"\
        +"================================"

if(__name__=="__main__"):
    evo=Evolution(population_size=47,genome_size=4,world_size=10,step_per_gen=300,mutation=0.1)
    print(repr(evo))
    
    evo.testGenEvolve(100)