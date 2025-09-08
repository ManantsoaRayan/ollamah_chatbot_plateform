import numpy as np

class Neuron:
    """
        A neuron: 
        takes inputs and product outputs
    """

    def __init__(self, weights: np.ndarray, bias, activation = None):
        self.weights = weights
        self.bias = bias
        self.activation = activation if activation is not None else lambda x:1/(1 + np.exp(-x))
        self.previous_sum = 0

    def feedforward(self, inputs:np.ndarray):
        sum_ = np.dot(inputs, self.weights)
        self.previous_sum = sum_
        return self.activation(sum)
        
class Model:
    """
        represent the model itself
    """

    def __init__(self, layer:int):
        pass