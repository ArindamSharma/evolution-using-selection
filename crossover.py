from genome import Genome,Gene,randint

class Crossover:

    def __init__(self,parent1,parent2,ctype=None,charCrossover=False,geneCrossover=False,crossoverpoint=None):
        """Corssover over Given parents as parameter """

        Crossover.verifyParent(parent1,parent2)
        if((charCrossover and geneCrossover)==False ):
            self.offspring=Genome(size=len(parent1))    
            self.offspring2=Genome(size=len(parent2))    
            # singlepoint
            if(ctype=="singlepoint" and charCrossover==True):
                self.offspring,self.offspring2=Crossover.NPointCharCrossover(parent1,parent2,1)
            elif(ctype=="singlepoint" and geneCrossover==True):
                self.offspring,self.offspring2=Crossover.NPointGeneCrossover(parent1,parent2,1)
            
            # multipoint
            elif(ctype=="multipoint" and charCrossover==True):
                self.offspring,self.offspring2=Crossover.NPointCharCrossover(parent1,parent2,crossoverpoint)
            elif(ctype=="multipoint" and geneCrossover==True):
                self.offspring,self.offspring2=Crossover.NPointCharCrossover(parent1,parent2,crossoverpoint)

            # uniform
            elif(ctype=="uniform" and charCrossover==True):
                self.offspring,self.offspring2=Crossover.UniformCharCrossover(parent1,parent2)
            elif(ctype=="uniform" and geneCrossover==True):
                self.offspring,self.offspring2=Crossover.UniformCharCrossover(parent1,parent2)

            # default
            elif(ctype==None and charCrossover==True):
                self.offspring,self.offspring2=Crossover.NPointCharCrossover(parent1,parent2,1)
            elif(ctype==None and geneCrossover==True):
                self.offspring,self.offspring2=Crossover.NPointGeneCrossover(parent1,parent2,1)
                
        else:
            raise Exception("CharCrossover and geneCrossover Cannot be True Together")

    def verifyParent(parent1:Genome,parent2:Genome)->bool:
        if(isinstance(parent1,Genome) and isinstance(parent2,Genome) and len(parent1)==len(parent2)):
            return True
        raise Exception("Invalid Parents")

    def UniformCharCrossover(parent1:Genome,parent2:Genome)->tuple(Genome):
        """CrossOver over two parents Uniformly (to all location)"""

        Crossover.verifyParent(parent1,parent2)
            
        childGenome1=Genome(size=len(parent1))
        # childGenome2=Genome(size=len(parent2))

        for i in range(len(parent2)*Gene.size):
            if(randint(0,1)):
                childGenome1[i//Gene.size][i%Gene.size]=parent1[i//Gene.size][i%Gene.size]
                # childGenome2[i//Gene.size][i%Gene.size]=parent2[i//Gene.size][i%Gene.size]
            else:
                childGenome1[i//Gene.size][i%Gene.size]=parent2[i//Gene.size][i%Gene.size]
                # childGenome2[i//Gene.size][i%Gene.size]=parent1[i//Gene.size][i%Gene.size]

    def UniformGeneCrossover(parent1:Genome,parent2:Genome)->tuple(Genome):
        """CrossOver Gene over two parents uniformly (to all gene)"""

        Crossover.verifyParent(parent1,parent2)

        childGenome1=[]
        # childGenome2=[]

        if (crossoverpoint>1):
            raise Exception("Havent wrote code for crossover more than 1")

        x=randint(0,len(parent1)-1)
        childGenome1.extend(parent1[:x]+parent2[x:])
        # childGenome2.extend(parent2[:x]+parent1[x+1:])

    def NPointCharCrossover(parent1:Genome,parent2:Genome,crossoverpoint:int)->tuple(Genome):
        """CrossOver over two parents from n crossover point which is set at random """

        Crossover.verifyParent(parent1,parent2)

        childGenome1=Genome(size=len(parent1))        
        # childGenome2=Genome(size=len(parent2))

        if (crossoverpoint>1):
            raise Exception("Havent wrote code for crossover more than 1")

        x=randint(0,len(parent1)*Gene.size-1)
        for i in range(len(parent1)*Gene.size):
            if(i<=x):
                childGenome1[i//Gene.size][i%Gene.size]=parent1[i//Gene.size][i%Gene.size]
                # childGenome2[i//Gene.size][i%Gene.size]=parent2[i//Gene.size][i%Gene.size]
            else:
                childGenome1[i//Gene.size][i%Gene.size]=parent2[i//Gene.size][i%Gene.size]
                # childGenome2[i//Gene.size][i%Gene.size]=parent1[i//Gene.size][i%Gene.size]
    
    def NPointGeneCrossover(parent1:Genome,parent2:Genome,crossoverpoint:int)->tuple(Genome):
        """CrossOver Gene over two parents from n crossover point which is set at random """

        Crossover.verifyParent(parent1,parent2)

        childGenome1=[]
        # childGenome2=[]

        if (crossoverpoint>1):
            raise Exception("Havent wrote code for crossover more than 1")

        x=randint(0,len(parent1)-1)
        childGenome1.extend(parent1[:x]+parent2[x:])
        # childGenome2.extend(parent2[:x]+parent1[x+1:])

if(__name__=="__main__"):
    parent1=Genome(size=4)
    parent2=Genome(size=4)
    Crossover(parent1,parent2)