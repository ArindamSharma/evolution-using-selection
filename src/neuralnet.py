from os import link
from encode import Connection
from random import randint

from neurons import InnerNeuron, SensorNeuron,ActionNeuron
from utils import Pair

class NeuralNet():
    
    def __init__(self,linkArray:list[Connection],inner_neuron:int=1):
        InnerNeuron.initNeuron(inner_neuron)
        self.sensor_neuron_array:dict[int,SensorNeuron]={}
        self.inner_neuron_array:dict[int,InnerNeuron]={}
        self.action_neuron_array:dict[int,ActionNeuron]={}
        self.age=0
        self.direction={
            0:"N",
            1:"NE",
            2:"E",
            3:"EW",
            4:"W",
            5:"WS",
            6:"S",
            7:"SE",
        }
        self.current_direction=randint(0,7)
        self.translateConnection(linkArray)
        self.linkArray=linkArray

    def translateConnection(self, linkArray:list[Connection]):
        self.sensor_neuron_id_array=set()
        self.inner_neuron_id_array=set()
        self.action_neuron_id_array=set()
        for link in linkArray:
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

        print([[i.source_add,i.dest_add,i.weight] for i in linkArray])

        for sensor_id in self.sensor_neuron_id_array:
            self.sensor_neuron_array[sensor_id]=SensorNeuron(sensor_id)
        for sensor_id in self.inner_neuron_id_array:
            self.inner_neuron_array[sensor_id]=InnerNeuron(sensor_id)
        for sensor_id in self.action_neuron_id_array:
            self.action_neuron_array[sensor_id]=ActionNeuron(sensor_id)


        for link in linkArray:
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
        # self.sensor_neuron_id_array=set(i.source_add for i in linkArray if i.source_id==0)
        # self.inner_neuron_id_array=set(i.source_add for i in linkArray if i.source_id==1).add(set(i.dest_add for i in linkArray if i.dest_id==0))
        # self.action_neuron_id_array=set(i.dest_add for i in linkArray if i.dest_id==1)
        # print(linkArray)
        # print("S",[i.source_add for i in linkArray if i.source_id==0])
        # print("I",
        #         [i.source_add for i in linkArray if i.source_id==1]+
        #         [i.dest_add for i in linkArray if i.dest_id==0]
        # )
        # print("O",[i.dest_add for i in linkArray if i.dest_id==1])
        print(self.sensor_neuron_id_array,self.inner_neuron_id_array,self.action_neuron_id_array)
        
        print("Sensor", [self.sensor_neuron_array[i].next for i in self.sensor_neuron_array])
        print("Inner",[self.inner_neuron_array[i].next for i in self.inner_neuron_array])
        print("Action",[self.action_neuron_array[i].value for i in self.action_neuron_array])

        print(self.sensor_neuron_array,self.inner_neuron_array,self.action_neuron_array)
        # print(self.sensor_neuron_id_array,self.inner_neuron_id_array,self.action_neuron_id_array)

    def getGenome():pass

    def __str__(self) -> str:
        return str(self.linkArray)