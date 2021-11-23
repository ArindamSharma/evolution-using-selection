import numpy as np
class NeuralNetwork:
    def __init__(self,input_neurons:list[int],number_of_hidden_layer:list[int],output_neurons:list[int]):
        """Parameters:
            input_neurons takes list of neurons (i.e Input Layer)
            number_of_hidden_layer takes list of sizes of each hidden layer (i.e array of hidden Layer sizes)
            output_neurons takes list of output neurons (i.e Output Layer)
        """
        self.layer1=np.array(input_neurons)
        self.layerH=self.generateHiddenLayers(number_of_hidden_layer)
        self.layerN=np.array(output_neurons)
        # np.random.seed(1)
        self.weight=self.generateWeight([self.layer1,*self.layerH,self.layerN])
    
    def generateHiddenLayers(self,array_of_sizes:list[int]):
        return np.array([np.zeros(size) for size in array_of_sizes])

    def generateWeight(self,layers:list[list[int]]):
        print(layers)
        print(np.random.random((3,4)))
        pass
    
    def feedForward(self,):
        pass

    def backPropogate(self,):
        pass
    
    def activation(self,x,deriv=False):
        if (deriv==True):
            return x(1-x)
        return 1/(1+np.exp(-x))
    
if __name__=="__main__":
    test_nn= NeuralNetwork(
        number_of_hidden_layer=[3],
        input_neurons=[
            [0,0,1],
            [1,1,1],
            [1,0,1],
            [0,1,1],
        ],
        output_neurons=[0,1,1,0]
    )