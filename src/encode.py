from genome import Genome
from connection import ConnectionArray,Connection

class Encode():
    """Neuron Encoding to Genome
    """
    def __init__(self,linkArray: ConnectionArray):
        self.genome=Genome(genome=self.encode(linkArray))

    def encode(self,linkArray:ConnectionArray)->str|Genome:
        genome=""
        for link in linkArray:
            genome+=str(link.generateGene())
        return genome

class Decode():
    """Genome Decoding 
    """
    def __init__(self,genome:Genome):
        self.linkArray:ConnectionArray=[]
        for i in genome.genome:
            self.linkArray.append(Connection(i))
    
    def __str__(self)->str:
        return str(self.linkArray)

if(__name__=="__main__"):
    genome=Genome(size=10)
    print(genome,Encode(Decode(genome).linkArray).genome,sep="\n")