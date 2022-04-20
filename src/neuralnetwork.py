import numpy as np
class NeuralNetwork:
    def __init__(self,input_neurons:list[int],number_of_hidden_layer:list[int],output_neurons:list[int]):
        """Parameters:
            input_neurons takes list of neurons (i.e Input Layer)
            number_of_hidden_layer takes list of sizes of each hidden layer (i.e array of hidden Layer sizes)
            output_neurons takes list of output neurons (i.e Output Layer)
        """
        self.layer1=np.array(input_neurons)[np.newaxis].T
        self.layerH=self.generateHiddenLayers(number_of_hidden_layer)
        self.layerN=np.array(output_neurons)[np.newaxis].T
        self.layer=[self.layer1,self.layerH,self.layerN]
        self.weight=self.generateWeight()
        self.weight_shape=[i.shape for i in self.weight]
    
    def generateHiddenLayers(self,array_of_sizes:list[int]):
        return np.array([np.zeros(size)[np.newaxis].T for size in array_of_sizes])
    
    def generateWeight(self,):
        layer_size_array=[len(i) for i in [self.layer1,*self.layerH,self.layerN]]
        return [2*np.random.random((layer_size_array[i+1],layer_size_array[i]))-1 for i in range(len(layer_size_array)-1)]
    
    def feedForward(self,):
        for current_layer_index in range(len(self.layer)-1):
            tmp=np.dot(self.weight[current_layer_index],self.layer[current_layer_index])
            self.layer[current_layer_index+1]=self.activation(tmp)
        print("Output Layer ",self.layer[-1].T)
    
    def backPropogate(self,):
        ol_error=self.layerN-self.layer[-1]
        print(ol_error.T)
        ol_delta=ol_error*self.activation(self.layer[-1],deriv=True)
        pass
    
    def activation(self,x,deriv=False):
        if (deriv==True):
            return x*(1-x)
        return 1/(1+np.exp(-x))
    
if __name__=="__main__":
    test_nn= NeuralNetwork(
        number_of_hidden_layer=[3],
        input_neurons=[1,0,1,0,1,0,0,1,1,0,1,1,0,1],
        output_neurons=[0,1,1,0]
    )
    for i in range(1):
        test_nn.feedForward()
        test_nn.backPropogate()