from random import randint
from creature import Creature
from genome import Genome

class World():
    def __init__(self,world_size=100):
        self.world_size=world_size
        self.population=0

        # self.matrixWorld=[]
        # self.generateWorld()
        
        self.unusedLocation=[]
        self.usedLocation={}
        self.refreshLocation()
        

    # def generateWorld(self,)->None:
    #     '''one time operation which creates the world for a give size'''
    #     for i in range(self.world_size):
    #         tmp=[]
    #         for j in range(self.world_size):
    #             tmp.append(None)
    #         self.matrixWorld.append(tmp)
    #     print("World Generated")

    def refreshLocation(self)->None:
        '''Clear/Refresh the world '''
        self.unusedLocation.clear()
        for i in range(self.world_size):
            for j in range(self.world_size):
                self.unusedLocation.append((i,j))
        self.usedLocation.clear()
        # print("Location Refreshed")

    def populateWorld(self,creatureArray:list[Creature])->None:
        for i in creatureArray:
            self.usedLocation[self.occupyRandomEmptyLocation()]=i

    def getEmptyLocation(self)-> tuple:
        '''This function return any random empty location '''
        upperlimit=(self.world_size*self.world_size)-self.population-1
        self.populationExceedCheck()
        return self.unusedLocation[randint(0,upperlimit)]

    def markLocationUsed(self,coordinate:tuple)->tuple:
        self.population+=1
        self.unusedLocation.remove(coordinate)
        return coordinate

    def occupyRandomEmptyLocation(self)->tuple:
        return self.markLocationUsed(self.getEmptyLocation())

    def populationExceedCheck(self)->None:
        if(self.population>(self.world_size*self.world_size)):
            raise ValueError("Population Limit Exceed :Max population can be "+str(self.world_size*self.world_size))

    def __str__(self):
        return ("========================\n"+
            "Matrx Size:".ljust(20," ")+" {}\n"+
            "Given-Population:".ljust(20," ")+" {}\n"+
            "Max-Population:".ljust(20," ")+" {}\n"+
            "========================"
            ).format(self.world_size,self.population,self.world_size*self.world_size)

if(__name__=="__main__"):
    matrix=World(10)
    # print(matrix.unusedLocation)
    matrix.populateWorld([Creature(Genome(size=4)) for i in range(47)])
    print(matrix.usedLocation)
    print(matrix.unusedLocation)
    print(list(matrix.usedLocation.keys())[0])
    print(matrix.usedLocation[(0,2)])
    print(matrix)