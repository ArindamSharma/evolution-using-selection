from encode import Connection, Encode
from genome import Gene, Genome

from neurons import InnerNeuron, SensorNeuron,ActionNeuron
# from creature import Creature
from utils import Pair

class NeuralNet():
    
    def __init__(self,linkArray:list[Connection],inner_neuron:int=1):
        # self.parent=parent
        
        InnerNeuron.initNeuron(inner_neuron)
        self.sensor_neuron_array:dict[int,SensorNeuron]={}
        self.inner_neuron_array:dict[int,InnerNeuron]={}
        self.action_neuron_array:dict[int,ActionNeuron]={}
        self.age=0
        self.linkArray=linkArray
        print(linkArray)
        self.translateConnection()
        print(linkArray)
        self.updatedWeights()
        # print(linkArray)

    def translateConnection(self)->None:
        self.sensor_neuron_id_array=set()
        self.inner_neuron_id_array=set()
        self.action_neuron_id_array=set()

        # Converts Longer addresses of neuron to give range of neurons
        for link in self.linkArray:
            if(link.source_id==0):
                link.source_add%=SensorNeuron.SIZE
                self.sensor_neuron_id_array.add(link.source_add)
                if(link.dest_id==0):
                    link.dest_add%=InnerNeuron.SIZE
                    self.inner_neuron_id_array.add(link.dest_add)
                else:
                    link.dest_add%=ActionNeuron.SIZE
                    self.action_neuron_id_array.add(link.dest_add)
            else:
                link.source_add%=InnerNeuron.SIZE
                self.inner_neuron_id_array.add(link.source_add)
                if(link.dest_id==0):
                    link.dest_add%=InnerNeuron.SIZE
                    self.inner_neuron_id_array.add(link.dest_add)
                else:
                    link.dest_add%=ActionNeuron.SIZE
                    self.action_neuron_id_array.add(link.dest_add)

        # print([[i.source_add,i.dest_add,i.weight] for i in self.linkArray])
        # print(linkArray)

        # Creation of different neurons 
        for sensor_id in self.sensor_neuron_id_array:
            self.sensor_neuron_array[sensor_id]=SensorNeuron(sensor_id)
        for sensor_id in self.inner_neuron_id_array:
            self.inner_neuron_array[sensor_id]=InnerNeuron(sensor_id)
        for sensor_id in self.action_neuron_id_array:
            self.action_neuron_array[sensor_id]=ActionNeuron(sensor_id)

        # updating the neurons next value
        for link in self.linkArray:
            if(link.source_id==0 and link.dest_id==0):
                self.sensor_neuron_array[link.source_add].next.append(Pair(self.inner_neuron_array[link.dest_add],link.weight))
            elif(link.source_id==0 and link.dest_id==1):
                self.sensor_neuron_array[link.source_add].next.append(Pair(self.action_neuron_array[link.dest_add],link.weight))
            elif(link.source_id==1 and link.dest_id==0):
                self.inner_neuron_array[link.source_add].next.append(Pair(self.inner_neuron_array[link.dest_add],link.weight))
            elif(link.source_id==1 and link.dest_id==1):
                self.inner_neuron_array[link.source_add].next.append(Pair(self.action_neuron_array[link.dest_add],link.weight))
            else:
                raise Exception("Source type or destination type of conection is not defined")
        
        # print(InnerNeuron.neuronID)
        # self.sensor_neuron_id_array=set(i.source_add for i in self.linkArray if i.source_id==0)
        # self.inner_neuron_id_array=set(i.source_add for i in self.linkArray if i.source_id==1).add(set(i.dest_add for i in self.linkArray if i.dest_id==0))
        # self.action_neuron_id_array=set(i.dest_add for i in self.linkArray if i.dest_id==1)
        # print(linkArray)
        # print("S",[i.source_add for i in self.linkArray if i.source_id==0])
        # print("I",
        #         [i.source_add for i in self.linkArray if i.source_id==1]+
        #         [i.dest_add for i in self.linkArray if i.dest_id==0]
        # )
        # print("O",[i.dest_add for i in self.linkArray if i.dest_id==1])
        
        # print(self.sensor_neuron_id_array,self.inner_neuron_id_array,self.action_neuron_id_array)
        
        # print("Sensor", [self.sensor_neuron_array[i].next for i in self.sensor_neuron_array])
        # print("Inner",[self.inner_neuron_array[i].next for i in self.inner_neuron_array])
        # print("Action",[self.action_neuron_array[i].value for i in self.action_neuron_array])

        # print(self.sensor_neuron_array,self.inner_neuron_array,self.action_neuron_array)
        
        
        # print(self.sensor_neuron_id_array,self.inner_neuron_id_array,self.action_neuron_id_array)
        
    def feedForward(self)->None:
        for sensor in self.sensor_neuron_array:
            print(self.sensor_neuron_array[sensor],self.sensor_neuron_array[sensor].next)
            self.sensor_neuron_array[sensor].getSensorValue()
        for sensor in self.inner_neuron_array:
            print(self.inner_neuron_array[sensor],self.inner_neuron_array[sensor].next)
            self.inner_neuron_array[sensor].accumulateInput()

    def filterLinks(self):
        pass

    def updateLinkWeight(self,source_type,source_neuron_id,dest_type,dest_neuron_id,weight)->None:
        for link in self.linkArray:
            if(link.source_id==source_type and link.source_add==source_neuron_id and link.dest_id==dest_type and link.dest_add==dest_neuron_id):
                # link.weight=0
                link.weight=weight
        
    def updatedWeights(self)->None:
        for source in self.sensor_neuron_array:
            source_neuron:SensorNeuron=self.sensor_neuron_array[source]
            for source_link in source_neuron.next:
                dest_neuron:ActionNeuron|InnerNeuron=source_link.first
                weight=source_link.second
                if(isinstance(dest_neuron,InnerNeuron)):
                    self.updateLinkWeight(0,source_neuron.id,0,dest_neuron.id,weight)
                elif(isinstance(dest_neuron,ActionNeuron)):
                    self.updateLinkWeight(0,source_neuron.id,1,dest_neuron.id,weight)
                else:
                    raise Exception("Undefined Class type found while updating weights")
        for source in self.inner_neuron_array:
            source_neuron:InnerNeuron=self.inner_neuron_array[source]
            for source_link in source_neuron.next:
                dest_neuron:ActionNeuron|InnerNeuron=source_link.first
                weight=source_link.second
                if(isinstance(dest_neuron,InnerNeuron)):
                    self.updateLinkWeight(1,source_neuron.id,0,dest_neuron.id,weight)
                elif(isinstance(dest_neuron,ActionNeuron)):
                    self.updateLinkWeight(1,source_neuron.id,1,dest_neuron.id,weight)
                else:
                    raise Exception("Undefined Class type found while updating weights")

    def getGenome(self)->Genome:
        return Encode(self.linkArray).genome

    def __str__(self) -> str:
        return str(self.sensor_neuron_array)+"\n"+str(self.action_neuron_array)+"\n"+str(self.inner_neuron_array)

if(__name__=="__main__"):
    brain=NeuralNet([Connection(Gene()) for i in range(4)],1)
    brain.feedForward()