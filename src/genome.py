from random import randint

from neurons import InnerNeuron

class Gene:
    """Gene Consist of 8 HexaDeciamal value
    here one Gene represent a Connection of neuron"""
    size=8
    def __init__(self,gene:str=None,bin:str=None):
        '''Generate Gene if nothing is passes ,

        generate and verify Gene if gene str is passes ,

        generate gene is bin str is passes'''

        if (gene==None and bin==None):
            self.gene=""
            for i in range(self.size):
                self.gene+=Gene.randomHexaDecimalNumber()
            self.bin=self.generateBin()
        elif(gene!=None and bin==None):
            self.gene=self.geneVerify(gene)
            self.bin=self.generateBin()
        elif(bin!=None):
            self.bin=bin
            self.gene=self.geneVerify(self.generateGene())

    def geneVerify(self,strgene:str)->str:
        """Considering user wont pass char out of Hexadeciaml range """

        if(len(strgene)!=self.size):
            raise Exception("Invalid Gene :: length must be : "+str(Gene.size))
        try:
            int(strgene,16)
        except (ValueError):
            raise Exception("Invalid Gene :: Not a heax value")
        return strgene

    def randomHexaDecimalNumber()->str:
        return hex(randint(0,15))[2:]

    def generateBin(self)->str:
        '''generate gene from bin'''
        return format(int(self.gene,16),'0'+str(Gene.size*4)+'b')

    def generateGene(self)->str:
        '''generate bin from gene'''
        return format(int(self.bin,2),'0'+str(Gene.size)+'x')

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o,Gene) and self.gene==__o

    def __str__(self):
        return self.gene

    def __getitem__(self,x) -> str:
        return self.gene[x]

    def __setitem__(self,x,key:str) -> None:
        self.gene=self.gene[:x]+str(key)+self.gene[x+1:]

    def __repr__(self) -> str:
        return "Gene: "+self.gene

class Genome:
    ''' Genomes consist of array/sequence of Gene '''
    fill=" "
    def __init__(self,genome:str=None,size:int=None):
        """Genome Can be passes ,if passed type must be string """
        
        # self.genome=genome
        if(genome==None and size!=None):
            self.genome=self.__validateGenome(self.__generateSelf(size))
        if(genome!=None):
            self.genome=self.__verifyString(genome)
            # self.genome=self.__generateSelf()

    def __verifyString(self,__genome:str)->list[Gene]:
        """Considering user wont pass char out of Hexadeciaml range """

        if(len(__genome)%Gene.size!=0 or len(__genome)==0):
            raise Exception("input string is not a valid genome")
        tmp_genome:list[Gene]=[]
        self.__size=0
        for i in range(0,len(__genome),Gene.size):
            tmp_genome.append(Gene(__genome[i:i+Gene.size]))
            self.__size+=1
        return tmp_genome

    def __validateGenome(self,genome:list[Gene])->list[Gene]:
        '''all gene in passed genome is valid or not '''
        return genome

    def __generateSelf(self,__size:int)->list[Gene]:
        tmp_genome=[]
        for i in range(__size):
            tmp_genome.append(Gene())
        return tmp_genome

    def bin(self)->str:
        string=""
        for i in self.genome:
            string+=i.bin()+""
        return string
    
    def randomGenomeLocation(self)->int:
        return randint(0,len(self)*Gene.size-1)

    def __repr__(self):
        tmp_genome="Genome : "
        for i in self.genome:
            tmp_genome+=i.gene+Genome.fill
        return tmp_genome

    def __str__(self):
        tmp_genome=""
        for i in self.genome:
            tmp_genome+=i.gene
        return tmp_genome

    def __len__(self):
        return len(self.genome)

    def __getitem__(self,a):
        return self.genome[a//Gene.size][a%Gene.size]

    def __setitem__(self,a,key):
        self.genome[a//Gene.size][a%Gene.size]=key
    
if(__name__=="__main__"):
    genome1=Genome("".join([str(Gene()) for i in range(8)]))
    genome2=Genome(size=4)
    print(genome1)
    print(genome2,len(genome2))
    print(Gene(bin=Gene().bin))