from logging import raiseExceptions
from random import randint
class Gene:
    """Gene Consist of 8 HexaDeciamal value
    here one Gene represent a connevtion of neuron"""
    
    geneLen=8
    def __init__(self,gene=None):
        
        if (gene==None):
            self.gene=""
            for i in range(self.geneLen):
                self.gene+=hex(randint(0,15))[2:]
        else:
            self.gene=self.geneVerify(gene)

    def geneVerify(self,strgene):
        if(len(strgene)!=self.geneLen):
            raise Exception("Invalid Gene")
        try:
            int(strgene,16)
        except (ValueError):
            raise Exception("Invalid Gene")
        return strgene

    def __str__(self):
        return self.gene

    def __getitem__(self,x):
        return self.gene[x]

    def __setitem__(self,x,key:str):
        self.gene=self.gene[:x]+str(key)+self.gene[x+1:]

class Genome:
    ''' Genomes consist of array/sequence of Gene '''
    def __init__(self,genome=None,size=None):
        self.genome=genome
        self.size=size
        if(self.genome==None and size!=None):
            self.genome=self.generateSelf()
        else:
            self.genome=self.verify(genome)

    # def verify(self,genome):
    #     for i in genome:
    #         Gene.geneVerify(i)
    def generateSelf(self):
        tmp_genome=[]
        for i in range(self.size):
            tmp_genome.append(Gene())
        return tmp_genome

    def generateChildRandom(self,genomeParent1:list[Gene],genomeParent2:list[Gene],mituationRate:float):
        """Random CrossOver over two parents"""
        if(len(genomeParent1)!=len(genomeParent2)):
            raiseExceptions("parent Genome must be of same length")
            
        childGenome1=[Gene("00000000") for i in range(len(genomeParent1))]
        # childGenome2=[Gene("00000000") for i in range(len(genomeParent2))]

        for i in range(len(genomeParent2)*Gene.geneLen):
            if(randint(0,1)):
                childGenome1[i//Gene.geneLen][i%Gene.geneLen]=genomeParent1[i//Gene.geneLen][i%Gene.geneLen]
                # childGenome2[i//Gene.geneLen][i%Gene.geneLen]=genomeParent2[i//Gene.geneLen][i%Gene.geneLen]
            else:
                childGenome1[i//Gene.geneLen][i%Gene.geneLen]=genomeParent2[i//Gene.geneLen][i%Gene.geneLen]
                # childGenome2[i//Gene.geneLen][i%Gene.geneLen]=genomeParent1[i//Gene.geneLen][i%Gene.geneLen]
        
        return self.mituation(childGenome1,mituationRate)

    def generateChildCrossoverAnyPoint(self,genomeParent1:list[Gene],genomeParent2:list[Gene],mituationRate:float,crossoverpoint:int):
        """CrossOver over two parents from a crossover point which is set at random """
        if(len(genomeParent1)!=len(genomeParent2)):
            raiseExceptions("parent Genome must be of same length")

        childGenome1=[Gene("00000000") for i in range(len(genomeParent1))]
        # childGenome2=[Gene("00000000") for i in range(len(genomeParent2))]

        if (crossoverpoint>1):
            raise Exception("Havent wrote code for crossover more than 1")

        x=randint(0,len(genomeParent1)*Gene.geneLen-1)
        for i in range(len(genomeParent1)*Gene.geneLen):
            if(i<=x):
                childGenome1[i//Gene.geneLen][i%Gene.geneLen]=genomeParent1[i//Gene.geneLen][i%Gene.geneLen]
                # childGenome2[i//Gene.geneLen][i%Gene.geneLen]=genomeParent2[i//Gene.geneLen][i%Gene.geneLen]
            else:
                childGenome1[i//Gene.geneLen][i%Gene.geneLen]=genomeParent2[i//Gene.geneLen][i%Gene.geneLen]
                # childGenome2[i//Gene.geneLen][i%Gene.geneLen]=genomeParent1[i//Gene.geneLen][i%Gene.geneLen]
        
        return self.mituation(childGenome1,mituationRate)

    def generateChildCrossoverGene(self,genomeParent1:list[Gene],genomeParent2:list[Gene],mituationRate:float,crossoverpoint:int):
        """CrossOver over two parents from a crossover point which is set at random """
        if(len(genomeParent1)!=len(genomeParent2)):
            raiseExceptions("parent Genome must be of same length")

        childGenome1=[]
        # childGenome2=[]

        if (crossoverpoint>1):
            raise Exception("Havent wrote code for crossover more than 1")

        x=randint(0,len(genomeParent1)-1)
        childGenome1.extend(genomeParent1[:x]+genomeParent2[x:])
        # childGenome2.extend(genomeParent2[:x]+genomeParent1[x+1:])
                
        return self.mituation(childGenome1,mituationRate)
    
    def mituation(self,genome,mrate):
        return genome

    def __str__(self):
        tmp_genome=""
        for i in self.genome:
            tmp_genome+=i.gene+" "
        return tmp_genome

    def __len__(self):
        return len(self.genome)

    def __getitem__(self,a):
        return self.genome[a//Gene.geneLen][a%Gene.geneLen]

    def __setitem__(self,a,key):
        self.genome[a//Gene.geneLen][a%Gene.geneLen]=key
    
if(__name__=="__main__"):
    genome1=Genome(size=4)
    genome2=Genome(size=4)
    print("Parent1 :",genome1)
    print("Parent2 :",genome2)
    # print()
    print("Crossover PointAny :",*genome1.generateChildCrossoverAnyPoint(genome1.genome,genome2.genome,mituationRate=0.01,crossoverpoint=1),sep=" ")
    print("Crossover Random   :",*genome1.generateChildRandom(genome1.genome,genome2.genome,mituationRate=0.01),sep=" ")
    print("Crossover Random   :",*genome1.generateChildCrossoverGene(genome1.genome,genome2.genome,mituationRate=0.01,crossoverpoint=1),sep=" ")
    # genome4=Genome(genomeParent1=genome1,genomeParent2=genome2,mituationRate=0.01)
    # print("Random Crossover      :",genome4)
    # for i in genome3.genome:
    #     print(bin(int(i,16))[2:].rjust(4,"0"),end=" ")
