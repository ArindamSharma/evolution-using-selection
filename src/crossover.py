from genome import Genome,Gene,randint

class Crossover:
    MULTIPOINT="multipoint"
    SINGLEPOINT="singlepoint"
    UNIFORM="uniform"
    def __init__(self,parent1:Genome,parent2:Genome,ctype:str=None,charCrossover=False,geneCrossover=False,crossoverpoint:int=None):
        """Corssover over Given parents as parameter """

        self.verifyParent(parent1,parent2)
        if((charCrossover and geneCrossover)==False ):
            self.offspring=Genome(size=len(parent1))    
            self.offspring2=Genome(size=len(parent2))    
            # singlepoint
            if(ctype==Crossover.SINGLEPOINT and charCrossover==True):
                self.NPointCharCrossover(parent1,parent2,1)
            elif(ctype==Crossover.SINGLEPOINT and geneCrossover==True):
                self.NPointGeneCrossover(parent1,parent2,1)
            
            # multipoint
            elif(ctype==Crossover.MULTIPOINT and charCrossover==True):
                self.NPointCharCrossover(parent1,parent2,crossoverpoint)
            elif(ctype==Crossover.MULTIPOINT and geneCrossover==True):
                self.NPointCharCrossover(parent1,parent2,crossoverpoint)

            # uniform
            elif(ctype==Crossover.UNIFORM and charCrossover==True):
                self.UniformCharCrossover(parent1,parent2)
            elif(ctype==Crossover.UNIFORM and geneCrossover==True):
                self.UniformCharCrossover(parent1,parent2)

            # default
            elif(ctype==None and charCrossover==True):
                self.NPointCharCrossover(parent1,parent2,1)
            elif(ctype==None and geneCrossover==True):
                self.NPointGeneCrossover(parent1,parent2,1)
                
        else:
            raise Exception("CharCrossover and geneCrossover Cannot be True Together")

    def verifyParent(self,parent1:Genome,parent2:Genome)->bool:
        if(isinstance(parent1,Genome) and isinstance(parent2,Genome) and len(parent1)==len(parent2)):
            return True
        raise Exception("Invalid Parents : "+str(parent1)+" and "+str(parent2))

    def UniformCharCrossover(self,parent1:Genome,parent2:Genome)->None:
        """CrossOver over two parents Uniformly (to all location)"""

        # self.verifyParent(parent1,parent2)
        for i in range(len(parent2)*Gene.size):
            if(randint(0,1)):
                self.offspring[i]=parent1[i]
                self.offspring2[i]=parent2[i]
            else:
                self.offspring[i]=parent2[i]
                self.offspring2[i]=parent1[i]

    def UniformGeneCrossover(self,parent1:Genome,parent2:Genome)->None:
        """CrossOver Gene over two parents uniformly (to all gene)"""

        # self.verifyParent(parent1,parent2)
        for i in range(len(parent2)):
            if(randint(0,1)):
                self.offspring.genome[i]=parent1.genome[i]
                self.offspring2.genome[i]=parent2.genome[i]
            else:
                self.offspring.genome[i]=parent2.genome[i]
                self.offspring2.genome[i]=parent1.genome[i]

    def NPointCharCrossover(self,parent1:Genome,parent2:Genome,crossoverpoint:int)->None:
        """CrossOver over two parents from n crossover point which is set at random 
        Note : crossoverpoint can be less than equal to passed parameter"""

        # self.verifyParent(parent1,parent2)
        x=[parent1.randomGenomeLocation() for _ in range(crossoverpoint)]
        flag=1
        for i in range(len(parent1)*Gene.size):
            if(i in x):
                flag*=-1

            if(flag==1):
                self.offspring[i]=parent1[i]
                self.offspring2[i]=parent2[i]
            else:
                self.offspring[i]=parent2[i]
                self.offspring2[i]=parent1[i]
    
    def NPointGeneCrossover(self,parent1:Genome,parent2:Genome,crossoverpoint:int)->None:
        """CrossOver Gene over two parents from n crossover point which is set at random 
        Note : crossoverpoint can be less than equal to passed parameter"""

        # Crossover.verifyParent(parent1,parent2)
        x=[parent1.randomGenomeLocation() for _ in range(crossoverpoint)]
        flag=1
        for i in range(len(parent1)):
            if(i in x):
                flag*=-1

            if(flag==1):
                self.offspring.genome[i]=parent1.genome[i]
                self.offspring2.genome[i]=parent2.genome[i]
            else:
                self.offspring.genome[i]=parent2.genome[i]
                self.offspring2.genome[i]=parent1.genome[i]

if(__name__=="__main__"):
    parent1=Genome(size=4)
    parent2=Genome(size=4)
    print(repr(parent1))
    print(repr(parent2))
    print(repr(Crossover(parent1,parent2,Crossover.MULTIPOINT,charCrossover=True,crossoverpoint=4).offspring))