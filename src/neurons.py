from genome import Gene
from utils import Pair

class SensorNeuron():
    neuronID=[
        "Age",# Sensitive to Age of Neuron
        "LocX",# Sensitive to Location from X axis
        "LocY",# Sensitive to Location from Y axis
        "BdDx",# Sensitive to Border Distance from X axis
        "BdDy",# Sensitive to Border Distance from Y axis
        "BdDb",# Sensitive to Border Distance from Both axis
        "LMvX",# Sensitive to Last Movement in X axis
        "LMvY",# Sensitive to Last Movement in Y axis
        "SIGN1",# Sensitive to Genetic Similarity In Adjacent Neighbour
        "SPhD",# Sensitive to Phermone Density in World
        "SPhDx",# Sensitive to Phermone Density X axis
        "SPhDy",# Sensitive to Phermone Density Y axis
        "PopD",# Sensitive to Phermone Density in World
        "PopDx",# Sensitive to Phermone Density in X axis
        "PopDy",# Sensitive to Phermone Density in Y axis
        "RnI",# Random Input
        "BlkL",# Blockage in Left 
        "BlkR",# Blockage in Right 
        "BlkFw",# Blockage in Front 
        "BlkBw",# Blockage in Back 
        "OSC",#Sensitive to Oscillation of Itself

        # phermone_gradient_forward_reverse
        # phermone_gradient_left_right
        # population_gradient_forward_reverse
        # population_gradient_left_right
    ]
    SIZE=len(neuronID)
    def __init__(self,neuronId:int):
        '''output range of sensory neurons is from 0.0 - 1.0'''
        self.id=neuronId
        self.code=SensorNeuron.neuronID[self.id]
        self.value=None
        self.next:list[Pair[InnerNeuron|ActionNeuron,Weight]]=[]


    def getSensorValue(self,neuron_id:int):
        pass

    def updateOutput(self):
        self.value=None

    def __str__(self)->str:
        return "Sensory Neuron ID "+str(self.id)+" Code "+str(self.code)+" "

    def __repr__(self)->str:
        return "Sensory "+str(self.code)+" "

class InnerNeuron():
    neuronID=[]
    SIZE=len(neuronID)
    def initNeuron(innerNeurons:int)->None:
        for i in range(innerNeurons):
            InnerNeuron.neuronID.append("I"+str(i))
            InnerNeuron.SIZE+=1

    def __init__(self,neuronId:str):
        '''output range of inner neuron is from -1.0 - 1.0'''
        self.input_neurons_value:list[float]=[]# previous neurons weighted values
        self.value=None
        self.id=neuronId
        self.code=InnerNeuron.neuronID[self.id]
        self.next:list[Pair[InnerNeuron|ActionNeuron,Weight]]=[]
        self.self_neuron=0
        
    def updateOutput(self):
        self.value=None

    def __str__(self)->str:
        return "Inner Neuron ID "+str(self.id)+" Code "+str(self.code)+" "

    def __repr__(self)->str:
        return "Inner "+str(self.code)+" "
        
class ActionNeuron():
    neuronID=[
        "MvRn",# Move Random
        "MvR",# Move Right
        "MvL",# Move Left
        "MvFw",# Move Forward
        "MvBw",# Move Backward
        "TnR",# Turn Right
        "TnL",# Turn Left
        "MvE",# Move East
        "MvW",# Move West
        "MvN",# Move North
        "MvS",# Move South
        "SRes",# Set Responsiveness
        "EmPh",# Emit Phermone to Adjacent Neighbour
        "OSC",# Oscillate
        "KFw",# Kill Forward
    ]
    SIZE=len(neuronID)
    def __init__(self,neuronId:int):
        '''output range of action neuron is from -1.0 - 1.0'''
        self.input_neurons_value:list[float]=[]# previous neurons weighted values
        self.value=None
        self.id=neuronId
        self.code=ActionNeuron.neuronID[self.id]

    def updateOutput(self):
        pass

    def __str__(self)->str:
        return "Action Neuron ID "+str(self.id)+" Code "+str(self.code)+" "

    def __repr__(self)->str:
        return "Action "+str(self.code)+" "


class Connection():
    '''Connection is a link information , contains source details ,destination details ,and weight details '''
    def __init__(self ,gene:Gene) -> None:
        self.source_id=int(gene.bin[0])
        self.source_add=int(gene.bin[1:8],2)
        self.dest_id=int(gene.bin[8])
        self.dest_add=int(gene.bin[9:16],2)
        self.weight=Weight(Connection.signed16bit(gene.bin[16:]))
        # if(self.source_id=='0'):
        #     self.source_id="S"
        #     # self.source_add%=SensorNeuron.number
        # else:
        #     self.source_id="I"
        #     # self.source_add%=InnerNeuron.number
        # if(self.dest_id=='0'):
        #     self.dest_id="I"
        # else:
        #     self.dest_id="O"

        # print(self.source_id,int(self.source_add,2),self.dest_id,int(self.dest_add,2),Connection.signed16bit(self.weight))
        self.array=(self.source_id,self.source_add,self.dest_id,self.dest_add,self.weight)
      
    def signed16bit(value:str)->int:
        if(value[0]=='1'):
            return int(value,2)-(1<<16)
            # return int(value,2)-2**16
        return int(value,2)
    
    def __str__(self) -> str:
        return " ".join([self.source_id,self.source_add,self.dest_id,self.dest_add,self.weight])

    def __repr__(self) -> str:
        return " ".join(str(i) for i in [self.source_id,self.source_add,self.dest_id,self.dest_add,self.weight])

class Weight():
    CONSTANT=(1<<15)/4
    '''weight should be in range of -4.0 - 4.0'''
    def __init__(self,weight:int):
        self.weight=weight/Weight.CONSTANT

    def __str__(self) -> str:
        return str(self.weight)

    def __repr__(self) -> str:
        return str(self.weight)

if __name__=="__main__":
    print(Weight.CONSTANT)