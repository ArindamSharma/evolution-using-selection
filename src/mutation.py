from genome import Genome,Gene

class Mutation:
    bitMutated=0
    modifiedLocation=[]
    RANDOMSWAP="randomswap"
    BITFLIP="bitflip"
    RANDOMRESET="randomreset"
    def __init__(self,genome:Genome=None,mrate:float=0.0,mtype:str="randomrandom"):
        """Mutates Genome inplace"""
        if(genome!=None and self.typeCheck(genome)):
            if(mtype=="randomswap"):
                genome=Mutation.RandomSwap(genome,mrate)
            elif(mtype=="bitflip"):
                genome=Mutation.BitFlip(genome,mrate)
            elif(mtype=="randomreset"):
                genome=Mutation.RandomResetting(genome,mrate)
            else: # "randomrandom" / default
                genome=Mutation.RandomRandom(genome,mrate)
        self.genome=genome

    def typeCheck(self,genome)->bool:
        if(isinstance(genome,Genome)):
            return True
        raise TypeError("Expected Genome Type to be Genome ,give ",type(genome))

    def __BitCal(mrate:float,genomeLength:int)->int:
        Mutation.bitMutated=int(genomeLength*Gene.size*mrate)
        return Mutation.bitMutated

    def BitFlip(genome:Genome,mrate:float)->None:
        """Inplace Updation : Mutation using mituation rate (can also be said as mituation probablity) 
        this is allpicable only in binary"""
        
    def RandomRandom(genome:Genome,mrate:float)->None:
        """Inplace Updation : Mutation using mituation rate (can also be said as mituation probablity) 
        random bit is set to any random hex character"""
        
        Mutation.modifiedLocation.clear()
        for _ in range(Mutation.__BitCal(mrate,len(genome))):
            loc=genome.randomGenomeLocation()
            Mutation.modifiedLocation.append(loc)
            genome[loc]=Gene.randomHexaDecimalNumber()

    def RandomResetting(genome:Genome,mrate:float)->None:
        """Inplace Updation : Mutation using mituation rate (can also be said as mituation probablity)
        resetting bits to its default value 0"""

        Mutation.modifiedLocation.clear()
        for _ in range(Mutation.__BitCal(mrate,len(genome))):
            loc=genome.randomGenomeLocation()
            Mutation.modifiedLocation.append(loc)
            # genome[loc]="f"
            genome[loc]="0"
        
    def RandomSwap(genome:Genome,mrate:float)->None:
        """Inplace Updation : Mutation using mituation rate (can also be said as mituation probablity)"""
        
        Mutation.modifiedLocation.clear()
        for _ in range(Mutation.__BitCal(mrate,len(genome))):
            loc1=genome.randomGenomeLocation()
            loc2=genome.randomGenomeLocation()
            Mutation.modifiedLocation.append(loc1)
            Mutation.modifiedLocation.append(loc2)
            # genome[loc]="f"
            genome[loc1],genome[loc2]=genome[loc2],genome[loc1]

if (__name__=="__main__"):
    genome=Genome(size=8)
    print(repr(genome))
    # Mutation.RandomRandom(genome,0.05)
    Mutation(genome,0.05,"randomreset")
    print(Mutation.modifiedLocation)
    print(repr(genome))