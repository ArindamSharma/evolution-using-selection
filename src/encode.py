from genome import Genome,Gene
from neurons import ActionNeurons,InnerNeurons,SensorNeurons

class Encode():
    """
    """
    def __init__(self,):
        pass

class Decode():
    """
    """
    def __init__(self,genome:Genome):
        for i in genome.genome:
            self.decode(i)

    def decode(self,gene:Gene)->tuple:
        print(gene.bin)
        print(gene.bin[0],gene.bin[1:10],gene.bin[10],gene.bin[11:20],gene.bin[20:32])
        if(gene.bin[0]=='0'):
            print("S:SensoryNeuron")
        else:
            print("S:Inner Neuron")
        print("S:",int(gene.bin[1:10],2))
        if(gene.bin[10]=='0'):
            print("D:Inner Neuron")
        else:
            print("D:ActionNeuron")
        print("D:",int(gene.bin[11:20],2))
        print("W:",int(gene.bin[20:32],2))


if(__name__=="__main__"):
    genome=Genome(size=4)
    brain=Decode(genome)