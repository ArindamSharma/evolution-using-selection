from utils import Pair
from weight import Weight
from math import tanh

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
        self.value:float=None
        self.next:list[Pair[InnerNeuron|ActionNeuron,Weight]]=[]

    def getSensorValue(self)->float:
        '''based on neuronID/sensor code extract sensor value'''
        if(self.code=="Age"):
            self.value=None
        elif(self.code=="LocX"):
            self.value=None
        return self.value

    def updateNext(self):
        '''after getting sensor value this function should be called'''
        if(self.value==None):
            raise Exception("getSencorValue method need to be called before calling updateNext method to update sensor value")
        for i in self.next:
            i.first.input_neuron_value.append(self.value*i.second)
        pass

    def __str__(self)->str:
        return "Sensory Neuron ID "+str(self.id)+" Code "+str(self.code)+" "

    def __repr__(self)->str:
        return "Sensory "+str(self.code)+" "
        # return "Sensory "+str(self.code)+" next ["+",".join([str(i.first) for i in self.next])+"]"

class InnerNeuron():
    neuronID=["I0"]
    SIZE=1
    def initNeuron(innerNeurons:int)->None:
        for i in range(1,innerNeurons):
            InnerNeuron.neuronID.append("I"+str(i))
            InnerNeuron.SIZE+=1

    def __init__(self,neuronId:str):
        '''output range of inner neuron is from -1.0 - 1.0'''
        self.input_neurons_value:list[float]=[]# previous neurons weighted values
        self.value:float= None
        self.id=neuronId
        self.code=InnerNeuron.neuronID[self.id]
        self.next:list[Pair[InnerNeuron|ActionNeuron,Weight]]=[]
        self.self_neuron=0
        
    def accumulateInput(self):
        self.value=tanh(sum(self.input_neurons_value))

    def updateNext(self):
        # TODO self loop code is not added now ,just ignored ,need to add in future

        if (self.value==None):
            raise Exception("There is no input to the neuron .this can occur if there is no incomming neuron to this neuron OR there accumlate Input function is not called")

        for neuron in self.next:
            if(neuron.first.id!=self.id):# ignoring self loop for now 
                neuron.first.input_neuron_value.append(neuron.second*self.value)

    def __str__(self)->str:
        return "Inner Neuron ID "+str(self.id)+" Code "+str(self.code)+" "

    def __repr__(self)->str:
        return "Inner "+str(self.code)+" "
        # return "Inner "+str(self.code)+" next ["+",".join([str(i.first) for i in self.next])+"]"
        
class ActionNeuron():
    neuronID=[
        "MvRn",# Move Random
        "MvR",# Move Right
        "MvL",# Move Left
        "MvFw",# Move Forward
        "MvBw",# Move Backward
        "TnR",# Turn Right
        "TnL",# Turn Left
        "TnR45",# Turn Right 45 degree
        "TnL45",# Turn Left 45 degree
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

    def accumulateInput(self):
        self.value=tanh(sum(self.input_neurons_value))

    def getActionValue(self):
        return self.value

    def __str__(self)->str:
        return "Action Neuron ID "+str(self.id)+" Code "+str(self.code)+" "

    def __repr__(self)->str:
        return "Action "+str(self.code)+" "

if __name__=="__main__":
    pass