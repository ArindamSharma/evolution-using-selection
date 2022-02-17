from logging import raiseExceptions
from random import randint
class Gene:
    """Gene Consist of 8 HexaDeciamal value
    here one Gene represent a connevtion of neuron"""
    
    size=8
    def __init__(self,gene=None):
        
        if (gene==None):
            self.gene=""
            for i in range(self.size):
                self.gene+=hex(randint(0,15))[2:]
        else:
            self.gene=self.geneVerify(gene)

    def geneVerify(self,strgene):
        if(len(strgene)!=self.size):
            raise Exception("Invalid Gene :: length must be : "+str(Gene.size))
        try:
            int(strgene,16)
        except (ValueError):
            raise Exception("Invalid Gene :: Not a heax value")
        return strgene

    def bin(self):
        return bin(int(self.gene,16))[2:].rjust(Gene.size*4,"0")

    def __str__(self):
        return self.gene

    def __getitem__(self,x) -> str:
        return self.gene[x]

    def __setitem__(self,x,key:str) -> None:
        self.gene=self.gene[:x]+str(key)+self.gene[x+1:]

    def __repr__(self) -> str:
        return "Hex: "+self.gene+"\n"+"Bin: "+ Gene.bin()

class Genome:
    ''' Genomes consist of array/sequence of Gene '''
    def __init__(self,genome=None,size=None):
        self.genome=genome
        self.__size=size
        if(genome==None and size!=None):
            self.genome=self.__generateSelf()
        if(genome!=None):
            self.genome=self.verify(genome)

    def verify(self,genome):
        tmp_genome=[]
        self.__size=0
        for i in genome:
            tmp_genome.append(Gene(i))
            self.__size+=1
        return tmp_genome

    def __generateSelf(self):
        tmp_genome=[]
        for i in range(self.__size):
            tmp_genome.append(Gene())
        return tmp_genome

    def generateChildRandom(self,genomeParent1:list[Gene],genomeParent2:list[Gene],mituationRate:float):
        """Public : Random CrossOver over two parents"""
        if(len(genomeParent1)!=len(genomeParent2)):
            raiseExceptions("parent Genome must be of same length")
            
        childGenome1=[Gene("00000000") for i in range(len(genomeParent1))]
        # childGenome2=[Gene("00000000") for i in range(len(genomeParent2))]

        for i in range(len(genomeParent2)*Gene.size):
            if(randint(0,1)):
                childGenome1[i//Gene.size][i%Gene.size]=genomeParent1[i//Gene.size][i%Gene.size]
                # childGenome2[i//Gene.size][i%Gene.size]=genomeParent2[i//Gene.size][i%Gene.size]
            else:
                childGenome1[i//Gene.size][i%Gene.size]=genomeParent2[i//Gene.size][i%Gene.size]
                # childGenome2[i//Gene.size][i%Gene.size]=genomeParent1[i//Gene.size][i%Gene.size]
        
        return Genome.mituation(childGenome1,mituationRate)

    def generateChildNPointCrossover(self,genomeParent1:list[Gene],genomeParent2:list[Gene],mituationRate:float,crossoverpoint:int):
        """Public : CrossOver over two parents from a crossover point which is set at random """
        if(len(genomeParent1)!=len(genomeParent2)):
            raiseExceptions("parent Genome must be of same length")

        childGenome1=[Gene("00000000") for i in range(len(genomeParent1))]
        # childGenome2=[Gene("00000000") for i in range(len(genomeParent2))]

        if (crossoverpoint>1):
            raise Exception("Havent wrote code for crossover more than 1")

        x=randint(0,len(genomeParent1)*Gene.size-1)
        for i in range(len(genomeParent1)*Gene.size):
            if(i<=x):
                childGenome1[i//Gene.size][i%Gene.size]=genomeParent1[i//Gene.size][i%Gene.size]
                # childGenome2[i//Gene.size][i%Gene.size]=genomeParent2[i//Gene.size][i%Gene.size]
            else:
                childGenome1[i//Gene.size][i%Gene.size]=genomeParent2[i//Gene.size][i%Gene.size]
                # childGenome2[i//Gene.size][i%Gene.size]=genomeParent1[i//Gene.size][i%Gene.size]
        
        return Genome.mituation(childGenome1,mituationRate)

    def generateChildNGeneCrossover(self,genomeParent1:list[Gene],genomeParent2:list[Gene],mituationRate:float,crossoverpoint:int):
        """Public : CrossOver over two parents from a crossover point which is set at random """
        if(len(genomeParent1)!=len(genomeParent2)):
            raiseExceptions("parent Genome must be of same length")

        childGenome1=[]
        # childGenome2=[]

        if (crossoverpoint>1):
            raise Exception("Havent wrote code for crossover more than 1")

        x=randint(0,len(genomeParent1)-1)
        childGenome1.extend(genomeParent1[:x]+genomeParent2[x:])
        # childGenome2.extend(genomeParent2[:x]+genomeParent1[x+1:])
                
        return Genome.mituation(childGenome1,mituationRate)
    
    def mituation(genome:list[Gene],mrate:int):
        """Public : Mutation using mituation rate """
        return genome

    def __str__(self):
        tmp_genome="Genome : "
        for i in self.genome:
            tmp_genome+=i.gene+" "
        return tmp_genome

    def bin(self):
        string=""
        for i in self.genome:
            string+=i.bin()+""
        return string

    def __len__(self):
        return len(self.genome)

    def __getitem__(self,a):
        return self.genome[a//Gene.size][a%Gene.size]

    def __setitem__(self,a,key):
        self.genome[a//Gene.size][a%Gene.size]=key
    
if(__name__=="__main__"):
    genome1=Genome(size=4)
    genome2=Genome(size=4)
    print(genome1)
    print(genome2)
    # print()
    print("Crossover PointAny :",*genome1.generateChildNPointCrossover(genome1.genome,genome2.genome,mituationRate=0.01,crossoverpoint=1),sep=" ")
    print("Crossover Random   :",*genome1.generateChildRandom(genome1.genome,genome2.genome,mituationRate=0.01),sep=" ")
    print("Crossover Gene     :",*genome1.generateChildNGeneCrossover(genome1.genome,genome2.genome,mituationRate=0.01,crossoverpoint=1),sep=" ")