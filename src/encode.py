from genome import Genome
from neurons import Connection

class Encode():
    """Neuron Encoding to Genome
    """
    def __init__(self,linkArray: list[Connection]):
        self.genome=Genome(genome=self.encode(linkArray))

    def encode(self,linkArray):
        pass

class Decode():
    """Genome Decoding 
    """
    def __init__(self,genome:Genome):
        self.linkArray:list[Connection]=[]
        for i in genome.genome:
            self.linkArray.append(Connection(i))
    
    def __str__(self)->str:
        return str(self.linkArray)

if(__name__=="__main__"):
    genome=Genome(size=24)
    print(Decode(genome))