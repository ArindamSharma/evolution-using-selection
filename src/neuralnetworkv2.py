from math import tanh
from random import randint
from connection import ConnectionArray
from weight import Weight
from compass import Compass

def mergeIdType(neuronid,neurontype):
    return ("I" if neurontype==0 else "A")+str(neuronid)

def seperateIdType(neuronid:str):
    '''Return (neurontype,neuronaddress)'''
    return ((0 if neuronid[0]=="I" else 1),int(neuronid[1:]))

class sensor():
    '''output range of sensory neurons is from 0.0 - 1.0'''
    def __init__(self,id,t,id2,w:Weight) -> None:
        self.id=id
        self.code=NeuralNetwork.SENSORYMAP[self.id]
        self.value=None
        self.next:dict[str,Weight]={mergeIdType(id2,t):w}

    def __str__(self) -> str:
        return "Sensor"+str(self.id)+" "+repr(self)
    def __repr__(self) -> str:
        return "["+",".join(["("+str(i)+","+str(self.next[i])+")" for i in self.next])+"]"

class inner():
    '''output range of inner neuron is from -1.0 - 1.0'''
    def __init__(self,id,t=None,id2=None,w:Weight=None) -> None:
        self.prev=[]
        self.id=id
        self.value=None
        if(t==None):
            self.next:dict[str,Weight]={}
        else:
            self.next:dict[str,Weight]={mergeIdType(id2,t):w}
    def accumulatePrev(self)->None:
        self.value=tanh(sum(self.prev))
    def __str__(self) -> str:
        return "Inner"+str(self.id)+" "+repr(self)
    def __repr__(self) -> str:
        return "["+",".join(["("+str(i)+","+str(self.next[i])+")" for i in self.next])+"]"

class action():
    '''output range of action neuron is from -1.0 - 1.0'''
    def __init__(self,id) -> None:
        self.prev=[]
        self.id=id
        self.code=NeuralNetwork.ACTIONMAP[self.id]
        self.value=None
    def accumulatePrev(self)->None:
        self.value=tanh(sum(self.prev))
    def __str__(self) -> str:
        return "Action"+str(self.id)+" "+repr(self)
    def __repr__(self) -> str:
        return "Value "+str(self.value)

class NeuralNetwork():

    def locx(self)->float:
        return self.body.location.x/self.simpara.world_size

    def locy(self)->float:
        return self.body.location.y/self.simpara.world_size
    
    def age(self)->float:
        return self.body.age/self.simpara.step_per_gen

    def bounderyX(self)->float:
        return min(self.body.location.x,self.simpara.world_size-self.body.location.x)/(self.simpara.world_size/2)

    def bounderyY(self)->float:
        return min(self.body.location.y,self.simpara.world_size-self.body.location.y)/(self.simpara.world_size/2)

    def boundery(self)->float:
        return (self.body.location.x+self.body.location.y)/(self.simpara.world_size*2)

    SENSORY={
        # '''output range of sensory neurons is from 0.0 - 1.0'''
        "Age":age,# Sensitive to Age of Neuron
        "LocX":locx,# Sensitive to Location from X axis
        "LocY":locy,# Sensitive to Location from Y axis
        "BdDx":bounderyX,# Sensitive to Border Distance from X axis
        "BdDy":bounderyY,# Sensitive to Border Distance from Y axis
        "BdDb":boundery,# Sensitive to Border Distance from Both axis
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

    def locationchecker(self,doubt_location)->bool:
        '''checks if the doubt location is empty of not'''
        # 1 check if location exist
        # 2 check if the location is empty 
        # TODO 3 check if location have some phermone :if yes update the creature
        #  

        # Step 1
        conditionx=doubt_location.x>=0 and doubt_location.x<self.simpara.world_size
        conditiony=doubt_location.y>=0 and doubt_location.y<self.simpara.world_size
        if(conditionx==False or conditiony==False):
            ##print("outside world",self.body.id)
            return False
        # Step 2 
        for creature in self.body.envLoc:
            # print("check ",doubt_location,creature.location)
            if (doubt_location==creature.location and creature.id!=self.body.id):
                # print("Location used")
                return False
        # Step 3
        return True

    # def move(self,direction,dependency):


    def mover(self)->None:
        # print(self.body.id,self.body.direction,"move right",self.body.location,end=",")
        doubt_location=self.body.direction.getNextLocation(self.body.location,Compass.RIGHT)
        ##print(self.body.id,doubt_location,self.locationchecker(doubt_location))
        if(self.locationchecker(doubt_location)):
            self.body.location=doubt_location
            ##print(doubt_location,end="")
        ##print()

    def movel(self)->None:
        # print(self.body.id,self.body.direction,"move left",self.body.location,end=",")
        doubt_location=self.body.direction.getNextLocation(self.body.location,Compass.LEFT)
        ##print(self.body.id,doubt_location,self.locationchecker(doubt_location))
        if(self.locationchecker(doubt_location)):
            self.body.location=doubt_location
            ##print(doubt_location,end="")
        ##print()
        
    def movef(self)->None:
        # print(self.body.id,self.body.direction,"move forward",self.body.location,end=",")
        doubt_location=self.body.direction.getNextLocation(self.body.location,Compass.FRONT)
        ##print(self.body.id,doubt_location,self.locationchecker(doubt_location))
        if(self.locationchecker(doubt_location)):
            self.body.location=doubt_location
            ##print(doubt_location,end="")
        ##print()

    def moveb(self)->None:
        # print(self.body.id,self.body.direction,"move backward",self.body.location,end=",")
        doubt_location=self.body.direction.getNextLocation(self.body.location,Compass.BACK)
        ##print(self.body.id,doubt_location,self.locationchecker(doubt_location))
        if(self.locationchecker(doubt_location)):
            self.body.location=doubt_location
            ##print(doubt_location,end="")
        ##print()

    def moverand(self)->None:        
        # print(self.body.id,self.body.direction,"move random",self.body.location,end=",")
        doubt_location=self.body.direction.getNextLocation(self.body.location,randint(-7,7))
        ##print(self.body.id,doubt_location,self.locationchecker(doubt_location))
        if(self.locationchecker(doubt_location)):
            self.body.location=doubt_location
            ##print(doubt_location,end="")
        ##print()

    def turnR90(self)->None:
        # print(self.body.id,self.body.direction,"Turn Right 90 ")
        self.body.direction.turn(2)

    def turnL90(self)->None:
        # print(self.body.id,self.body.direction,"Turn Left 90 ")
        self.body.direction.turn(-2)
        
    def turnR45(self)->None:
        # print(self.body.id,self.body.direction,"Turn Right 45 ")
        self.body.direction.turn(1)

    def turnL45(self)->None:
        # print(self.body.id,self.body.direction,"Turn Left 90 ")
        self.body.direction.turn(1)
        
    def moveE(self)->None:
        # print(self.body.id,self.body.direction,"move East",self.body.location,end=",")
        doubt_location=self.body.direction.getNextLocation(self.body.location,Compass.EAST,False)
        ##print(self.body.id,doubt_location,self.locationchecker(doubt_location))
        if(self.locationchecker(doubt_location)):
            self.body.location=doubt_location
            ##print(doubt_location,end="")
        ##print()

    def moveW(self)->None:
        # print(self.body.id,self.body.direction,"move West",self.body.location,end=",")
        doubt_location=self.body.direction.getNextLocation(self.body.location,Compass.WEST,False)
        ##print(self.body.id,doubt_location,self.locationchecker(doubt_location))
        if(self.locationchecker(doubt_location)):
            self.body.location=doubt_location
            ##print(doubt_location,end="")
        ##print()
        
    def moveN(self)->None:
        # print(self.body.id,self.body.direction,"move North",self.body.location,end=",")
        doubt_location=self.body.direction.getNextLocation(self.body.location,Compass.NORTH,False)
        ##print(self.body.id,doubt_location,self.locationchecker(doubt_location))
        if(self.locationchecker(doubt_location)):
            self.body.location=doubt_location
            ##print(doubt_location,end="")
        ##print()

    def moveS(self)->None:
        # print(self.body.id,self.body.direction,"move South",self.body.location,end=",")
        doubt_location=self.body.direction.getNextLocation(self.body.location,Compass.SOUTH,False)
        ##print(self.body.id,doubt_location,self.locationchecker(doubt_location))
        if(self.locationchecker(doubt_location)):
            self.body.location=doubt_location
            ##print(doubt_location,end="")
        ##print()

    ACTION={
        # '''output range of sensory neurons is from -1.0 - 1.0'''
        # direction specific
        "MvRn":moverand,# Move Random
        "MvR":mover,# Move Right
        "MvL":movel,# Move Left
        "MvFw":movef,# Move Forward
        "MvBw":moveb,# Move Backward
        "TnR":turnR90,# Turn Right
        "TnL":turnL90,# Turn Left
        "TnR45":turnR45,# Turn Right 45 degree
        "TnL45":turnL45,# Turn Left 45 degree
        "MvE":locx,# Move East
        "MvW":locx,# Move West
        "MvN":locx,# Move North
        "MvS":locx,# Move South
        # "SRes":locx,# Set Responsiveness
        # "EmPh":locx,# Emit Phermone to Adjacent Neighbour
        # "OSC":locx,# Oscillate
        # "KFw":locx,# Kill Forward
    }
    ACTIONMAP=[i for i in ACTION]

    def __init__(self,body,linklist:ConnectionArray,simparam) -> None:
        self.body=body
        self.simpara=simparam
        self.MAXINNERNEURON=simparam.inner_neuron

        self.sensor:dict[int,sensor]={}
        self.inner:dict[int,inner]={}
        self.action:dict[int,action]={}
        
        self.linklist=linklist
        self.translatelink()
        self.body.r=(len(self.sensor)*60)%255
        self.body.g=(len(self.inner)*60)%255
        self.body.b=(len(self.action)*60)%255
        # print(self.sensor)
        # print(self.inner)
        # print(self.action)
        # print()
        # print(self.linklist)
        
        # self.feedForward()
        # print(self.sensor)
        # print(self.inner)
        # print(self.action)
    
    
    def normalizeNeuronAd(self):
        for link in self.linklist:
            if(link.source_id==0):
                link.source_add%=len(NeuralNetwork.SENSORY)#sensor
            else:
                link.source_add%=self.MAXINNERNEURON#inner
            if(link.dest_id==0):
                link.dest_add%=self.MAXINNERNEURON#inner
            else:
                link.dest_add%=len(NeuralNetwork.ACTION)#action

    def translatelink(self):
        self.normalizeNeuronAd()

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

        # TODO Remove Useless Links is Important 
        # but its creating issue which deleting for the linklist which is creating problem in while updating weight
        # so after fixing the removeuselesslink code i will run that as well

        # self.removeUselessLink()

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
        # Getting reading from sensors
        self.getSensorReading()

        # Accumulating Sensor value
        for neuron_add in self.sensor:
            for neuron in self.sensor[neuron_add].next:
                id,add=seperateIdType(neuron)
                if(id==0):
                    self.inner[add].prev.append(self.sensor[neuron_add].value*self.sensor[neuron_add].next[neuron].value)
                else:
                    self.action[add].prev.append(self.sensor[neuron_add].value*self.sensor[neuron_add].next[neuron].value)
        # print([str(self.action[i].prev) for i in self.action])
        # Note :As of now self loop is ignored in the code
        # Updating next connected inner/action neurons
        for neuron_add in self.inner:
            self.inner[neuron_add].accumulatePrev()
            for neuron in self.inner[neuron_add].next:
                id,add=seperateIdType(neuron)
                if(id==0):
                    self.inner[add].prev.append(self.inner[neuron_add].value*self.inner[neuron_add].next[neuron].value)
                else:
                    self.action[add].prev.append(self.inner[neuron_add].value*self.inner[neuron_add].next[neuron].value)
            
            # print(self.inner[neuron_add])

        # Accumulating Action Neuron the previous vale 
        for neuron_add in self.action:
            self.action[neuron_add].accumulatePrev()
            # print(self.action[neuron_add])

        # Performing Action based on action neuron
        self.performAction()
        self.body.age+=1

    def getSensorReading(self)->None:
        for neuron_add in self.sensor:
            self.sensor[neuron_add].value=self.SENSORY[self.sensor[neuron_add].code](self)
        # print([str(self.sensor[i].value) for i in self.sensor])

    def performAction(self)->None:
        for neuron_add in self.action:
            if(self.action[neuron_add].value>=0.01):
                self.ACTION[self.action[neuron_add].code](self)

    def updateWeight(self):

        for link in self.linklist:
            # Sensor to Inner
            if(link.source_id==0 and link.dest_id==0):
                link.weight=self.sensor[link.source_add].next[mergeIdType(link.dest_add,0)]
            # Sensor to Action
            if(link.source_id==0 and link.dest_id==1):
                link.weight=self.sensor[link.source_add].next[mergeIdType(link.dest_add,1)]
            # Inner to Inner
            if(link.source_id==1 and link.dest_id==0):
                link.weight=self.inner[link.source_add].next[mergeIdType(link.dest_add,0)]
            # Inner to Action
            if(link.source_id==1 and link.dest_id==1):
                link.weight=self.inner[link.source_add].next[mergeIdType(link.dest_add,1)]

    def getConnectionList(self)->ConnectionArray:
        return self.linklist

    def __str__(self) -> str:
        return "Sensors:"+str(self.sensor)+" Inner:"+str(self.inner)+" Action:"+str(self.action)
if(__name__=="__main__"):
    pass
    # from connection import ConnectionArray,Connection
    # from genome import Gene
    # from evolution import SimParam
    # from creature import Creature
    # a=NeuralNetwork(Creature(),ConnectionArray([Connection(Gene()) for i in range(24)]),SimParam(inner_neuron=6))