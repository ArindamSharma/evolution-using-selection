from math import tanh
class neuron():
    def locx():
        pass

    def locy():
        pass
    
    def age():
        pass

    SENSORY={
        "Age":age,# Sensitive to Age of Neuron
        "LocX":locx,# Sensitive to Location from X axis
        "LocY":locx,# Sensitive to Location from Y axis
        # "BdDx":locx,# Sensitive to Border Distance from X axis
        # "BdDy":locx,# Sensitive to Border Distance from Y axis
        # "BdDb":locx,# Sensitive to Border Distance from Both axis
        # "LMvX":locx,# Sensitive to Last Movement in X axis
        # "LMvY":locx,# Sensitive to Last Movement in Y axis
        # "SIGN1":locx,# Sensitive to Genetic Similarity In Adjacent Neighbour
        # "SPhD":locx,# Sensitive to Phermone Density in World
        # "SPhDx":locx,# Sensitive to Phermone Density X axis
        # "SPhDy":locx,# Sensitive to Phermone Density Y axis
        # "PopD":locx,# Sensitive to Phermone Density in World
        # "PopDx":locx,# Sensitive to Phermone Density in X axis
        # "PopDy":locx,# Sensitive to Phermone Density in Y axis
        # "RnI":locx,# Random Input
        # "BlkL":locx,# Blockage in Left 
        # "BlkR":locx,# Blockage in Right 
        # "BlkFw":locx,# Blockage in Front 
        # "BlkBw":locx,# Blockage in Back 
        # "OSC":locx,#Sensitive to Oscillation of Itself
    }
    SENSORYMAP=[i for i in SENSORY]

    def mover():
        pass
    def movel():
        pass
    def moverand():
        pass
    
    ACTION={
        "MvRn":moverand,# Move Random
        "MvR":mover,# Move Right
        "MvL":movel,# Move Left
        # "MvFw":locx,# Move Forward
        # "MvBw":locx,# Move Backward
        # "TnR":locx,# Turn Right
        # "TnL":locx,# Turn Left
        # "TnR45":locx,# Turn Right 45 degree
        # "TnL45":locx,# Turn Left 45 degree
        # "MvE":locx,# Move East
        # "MvW":locx,# Move West
        # "MvN":locx,# Move North
        # "MvS":locx,# Move South
        # "SRes":locx,# Set Responsiveness
        # "EmPh":locx,# Emit Phermone to Adjacent Neighbour
        # "OSC":locx,# Oscillate
        # "KFw":locx,# Kill Forward
    }
    ACTIONMAP=[i for i in ACTION]

def mergeIdType(neuronid,neurontype):
    return ("I" if neurontype==0 else "A")+str(neuronid)
def seperateIdType(neuronid:str):
    '''Return (neurontype,neuronaddress)'''
    return ((0 if neuronid[0]=="I" else 1),int(neuronid[1:]))
class sensor():
    def __init__(self,id,t,id2,w) -> None:
        self.id=id
        self.code=neuron.SENSORYMAP[self.id]
        self.value=None
        self.next:dict[str,float]={mergeIdType(id2,t):w}

    def getValue(self)->int:
        return neuron.ACTION[self.code]()
    def __str__(self) -> str:
        return "Sensor"+str(self.id)+" "+repr(self)
    def __repr__(self) -> str:
        return "["+",".join(["("+str(i)+","+str(self.next[i])+")" for i in self.next])+"]"
class inner():
    def __init__(self,id,t=None,id2=None,w=None) -> None:
        self.prev=[]
        self.id=id
        self.value=None
        if(t==None):
            self.next:dict[str,float]={}
        else:
            self.next:dict[str,float]={mergeIdType(id2,t):w}
    def accumulatePrev(self)->None:
        self.value=tanh(sum(self.prev))
    def __str__(self) -> str:
        return "Inner"+str(self.id)+" "+repr(self)
    def __repr__(self) -> str:
        return "["+",".join(["("+str(i)+","+str(self.next[i])+")" for i in self.next])+"]"
class action():
    def __init__(self,id) -> None:
        self.prev=[]
        self.id=id
        self.code=neuron.ACTIONMAP[self.id]
        self.value=None
    def accumulatePrev(self)->None:
        self.value=tanh(sum(self.prev))
    def __str__(self) -> str:
        return "Action"+str(self.id)+" "+repr(self)
    def __repr__(self) -> str:
        return "Value "+str(self.value)

class NeuralNetwork(neuron):

    def __init__(self,linklist,inner_size) -> None:
        self.age=0
        self.MAXINNERNEURON=inner_size
        self.sensor:dict[int,sensor]={}
        self.inner:dict[int,inner]={}
        self.action:dict[int,action]={}
        self.linklist=linklist
        self.normalizeNeuronAd()
        self.translatelink()

        # print()
        # print("Last")
        # print(self.sensor)
        # print(self.inner)
        # print(self.action)
        # print(self.linklist)
        self.feedForward()
    
    def normalizeNeuronAd(self):
        for link in self.linklist:
            if(link.source_id==0):
                link.source_add%=len(self.SENSORY)#sensor
            else:
                link.source_add%=self.MAXINNERNEURON#inner
            if(link.dest_id==0):
                link.dest_add%=self.MAXINNERNEURON#inner
            else:
                link.dest_add%=len(self.ACTION)#action

    def translatelink(self):
        self.sensor.clear()
        self.inner.clear()
        self.action.clear()

        for link in self.linklist:
            if(link.source_id==0 and link.dest_id==0):
                # Sensor to Inner
                if(link.source_add in self.sensor):
                    self.sensor[link.source_add].next[mergeIdType(link.dest_add,link.dest_id)]=link.weight
                else:
                    self.sensor[link.source_add]=sensor(link.source_add,link.dest_id,link.dest_add,link.weight)
                if(link.dest_add not in self.inner):
                    self.inner[link.dest_add]=inner(link.dest_add)
            
            elif(link.source_id==0 and link.dest_id==1):
                # Sensor to Action
                if(link.source_add in self.sensor):
                    self.sensor[link.source_add].next[mergeIdType(link.dest_add,link.dest_id)]=link.weight
                else:
                    self.sensor[link.source_add]=sensor(link.source_add,link.dest_id,link.dest_add,link.weight)
                # self.sensor[link.source_add]=sensor(link.source_add)
                if(link.dest_add not in self.action):
                    self.action[link.dest_add]=action(link.dest_add)
                # self.action[link.dest_add]=action(link.dest_add)

            elif(link.source_id==1 and link.dest_id==0):
                # Inner To Inner
                if(link.source_add in self.inner):
                    self.inner[link.source_add].next[mergeIdType(link.dest_add,link.dest_id)]=link.weight
                else:
                    self.inner[link.source_add]=inner(link.dest_add,link.dest_id,link.dest_add,link.weight)
                # self.inner[link.source_add]=inner(link.source_add)
                if(link.dest_add not in self.inner):
                    self.inner[link.dest_add]=inner(link.dest_add)
                # self.inner[link.dest_add]=inner(link.dest_add)
            
            elif(link.source_id==1 and link.dest_id==1):
                # Inner To Action
                if(link.source_add in self.inner):
                    self.inner[link.source_add].next[mergeIdType(link.dest_add,link.dest_id)]=link.weight
                else:
                    self.inner[link.source_add]=inner(link.dest_add,link.dest_id,link.dest_add,link.weight)
                # self.inner[link.source_add]=inner(link.source_add)
                if(link.dest_add not in self.action):
                    self.action[link.dest_add]=action(link.dest_add)
                # self.action[link.dest_add]=action(link.dest_add)
                
            # print(self.sensor)
            # print(self.inner)
            # print(self.action)
            # print("")

        # print(self.linklist)
        # print(self.sensor)
        # print(self.inner)
        # print(self.action)
        # print("")
        
        self.removeUselessLink()

    def removeUselessLink(self):
        '''Removes useless connections 
        
        must run translate link method before this'''
        tmp_inner_neuron_add=[]
        # storing what inner neurons to remove
        for neuron_add in self.inner:
            if (len(self.inner[neuron_add].next)==0):
                tmp_inner_neuron_add.append(neuron_add)

        # print(self.linklist)
        # print(self.sensor)
        # print(self.inner)
        # print(self.action)
        # print(tmp_inner_neuron_add)
        # print("")

        if(len(tmp_inner_neuron_add)!=0):    
            # Removing from linklist
            for uwlink in tmp_inner_neuron_add:
                for link in self.linklist:
                    if((link.source_id==1 and link.source_add==uwlink )or(link.dest_id==0 and link.dest_add==uwlink)):
                        self.linklist.removeConnection(link)
            # Remove from all neurons
            # Removing from sensor
            for uwlink in tmp_inner_neuron_add:
                for add in self.sensor:
                    if(mergeIdType(uwlink,0) in self.sensor[add].next):
                        self.sensor[add].next.pop(mergeIdType(uwlink,0))

            # Removing sensor with no connection
            tmp_sensor_neuron_id=[]
            for add in self.sensor:
                if(len(self.sensor[add].next)==0):
                    tmp_sensor_neuron_id.append(add)
            for add in tmp_sensor_neuron_id:
                self.sensor.pop(add)

            # Removing from inner
            for uwlink in tmp_inner_neuron_add:
                self.inner.pop(uwlink)
                for add in self.inner:
                    if(mergeIdType(uwlink,0) in self.inner[add].next):
                        self.inner[add].next.pop(mergeIdType(uwlink,0))
            
            self.removeUselessLink()

    def feedForward(self):
        for neuron_add in self.sensor:
            print(self.sensor[neuron_add])
        for neuron_add in self.inner:
            self.inner[neuron_add].accumulatePrev()
            for neuron in self.inner[neuron_add].next:
                id,add=seperateIdType(neuron)
                if(id==0):
                    self.inner[add].prev.append(self.inner[neuron_add].value*self.inner[neuron_add].next[neuron].value)
                else:
                    self.action[add].prev.append(self.inner[neuron_add].value*self.inner[neuron_add].next[neuron].value)
            
            print(self.inner[neuron_add])
        for neuron_add in self.action:
            self.action[neuron_add].accumulatePrev()
            print(self.action[neuron_add])


if(__name__=="__main__"):
    from connection import ConnectionArray,Connection
    from genome import Gene
    a=NeuralNetwork(ConnectionArray([Connection(Gene()) for i in range(24)]),6)